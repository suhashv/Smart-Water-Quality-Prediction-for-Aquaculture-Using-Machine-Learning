from flask import Flask, render_template, jsonify
import requests
import numpy as np
import joblib
import tensorflow as tf
import os  

app = Flask(__name__)

# ThingSpeak Read API Key & Channel Info
API_KEY = "WY1D1435R5CVKWDN"
CHANNEL_ID = "2856767"
READ_URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={API_KEY}&results=1"

# Load the trained model
try:
    with open("model_architecture.json", "r") as json_file:
        model_json = json_file.read()
    model = tf.keras.models.model_from_json(model_json)
    model.load_weights("model_weights.weights.h5")  
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
except Exception as e:
    print("Error loading model:", e)
    exit()

# Load the scaler
scaler_path = "scaler.pkl"
if os.path.exists(scaler_path):
    try:
        scaler = joblib.load(scaler_path)
    except Exception as e:
        print("Error loading scaler:", e)
        exit()
else:
    print("Scaler file not found!")
    exit()

def get_sensor_data():
    """Fetch latest sensor values from ThingSpeak."""
    try:
        response = requests.get(READ_URL)
        data = response.json()
        
        if "feeds" in data and len(data["feeds"]) > 0:
            latest_entry = data["feeds"][-1]
            pH = float(latest_entry.get("field1", 0))  
            turbidity = float(latest_entry.get("field2", 0))
            solids = float(latest_entry.get("field3", 0))
            return np.array([[pH, turbidity, solids]]), pH, turbidity, solids
        return None, None, None, None
    except Exception as e:
        return None, None, None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    sensor_data, pH, turbidity, solids = get_sensor_data()
    if sensor_data is None:
        return jsonify({"error": "No sensor data available"})
    try:
        input_scaled = scaler.transform(sensor_data)
        input_reshaped = input_scaled.reshape(1, 1, sensor_data.shape[1])
        prediction = model.predict(input_reshaped)
        result = "Good" if prediction[0][0] > 0.5 else "Poor"
        return jsonify({
            "pH": round(pH, 2),
            "turbidity": round(turbidity, 2),
            "solids": round(solids, 2),
            "quality": result
        })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
