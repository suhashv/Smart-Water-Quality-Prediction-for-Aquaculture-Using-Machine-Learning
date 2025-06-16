# 🌊 Smart Water Quality Prediction for Aquaculture Using Machine Learning

This **capstone project** focuses on predicting water quality in aquaculture using advanced machine learning techniques. By analyzing water parameters such as **pH**, **turbidity**, and **potability**, this system helps monitor and ensure safe water conditions for aquatic life.  

⚡ The solution leverages **LSTM**, **GRU**, and **CNN models**, and is designed for real-time insights via a simple web app interface (Streamlit / Flask).  
⚡ The project also integrates **Firebase** for **real-time monitoring** and data updates, with a live website at 👉 [https://waterquality-1dcdc.web.app/](https://waterquality-1dcdc.web.app/)

---

## 🎯 Project Goals

✅ Predict water potability and quality from sensor data  
✅ Enable aquaculture managers to take action before water quality deteriorates  
✅ Build a modular, scalable, and deployable ML pipeline  
✅ Provide real-time water quality monitoring via Firebase  

---

## 🛠 Technologies Used

- **Python 3.x**
- **TensorFlow / Keras**
- **scikit-learn**
- **Pandas**, **NumPy**
- **Streamlit** / **Flask**
- **Firebase (Realtime Database, Hosting)**
- **Matplotlib**, **Seaborn**
- **HTML / CSS / JS** (for chatbot and frontend)

---

## 📁 Project Structure

```
smart-water-quality-prediction/
├── app.py                 # Main web application file
├── code/                  # Code files for processing and modeling
│   ├── convert.py
│   ├── labelingdata.py
│   ├── ML.py
│   ├── model_architecture.json
│   ├── model_weights.weights.h5
│   └── scaler.pkl
├── data/                  # Datasets
│   ├── augmented_water_data.xlsx
│   ├── water_data.xlsx
│   └── water_potability.xlsx
├── web/                   # Frontend files
│   └── fish_water_quality_chatbot.html
├── templates/              # HTML templates (if applicable)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/smart-water-quality-prediction.git
cd smart-water-quality-prediction
```

### 2️⃣ Install required packages
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application
```bash
python app.py
```
or if you are using **Streamlit**:
```bash
streamlit run app.py
```

---

## 📊 Example Dataset Columns

| Feature     | Description                    |
|-------------|--------------------------------|
| pH          | Acidity/alkalinity of water     |
| Turbidity   | Cloudiness / particle level     |
| Solids      | Total dissolved solids (ppm)    |
| Potability  | 1 = safe for drinking, 0 = unsafe |

---

## ✨ Features of This Project

🌟 Predict water potability using ML models  
🌟 Visualize input data trends  
🌟 Real-time water quality monitoring using Firebase  
🌟 Clean and minimal web app interface (link: [https://waterquality-1dcdc.web.app/](https://waterquality-1dcdc.web.app/))  
🌟 Modular code (easy to extend for new sensors / models)  
🌟 Ready for deployment on cloud or local servers  

---

## 💬 Fish Water Quality Chatbot

This project also includes a **Fish Water Quality Chatbot** built using **HTML, CSS, and JavaScript**. The chatbot connects to **Gemini API** to provide optimal water conditions for different fish species, including:

- Ideal pH range  
- Turbidity (NTU)  
- Total dissolved solids (mg/L)

✅ The chatbot features a clean, responsive design and is easy to extend or embed into other apps.  

👉 **File:** `web/fish_water_quality_chatbot.html`  

To try it:
1️⃣ Open the HTML file in any modern browser.  
2️⃣ Enter the name of a fish species and click **Get Water Conditions**.  
3️⃣ View the recommended water parameters retrieved via API.  

---

## 💡 Example Use Cases

- Automated monitoring in aquaculture ponds  
- Early detection of unsuitable water conditions  
- Integration into IoT-based smart aquaculture systems  

---

## 📄 License

This project is licensed under the **MIT License** — free to use and modify with attribution.

---


## 🔗 Live Demo

🌐 Real-time monitoring web app: [https://waterquality-1dcdc.web.app/](https://waterquality-1dcdc.web.app/)
