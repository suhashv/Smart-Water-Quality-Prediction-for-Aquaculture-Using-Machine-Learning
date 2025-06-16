# Smart-Water-Quality-Prediction-for-Aquaculture-Using-Machine-Learning
Capstone project that predicts water quality for aquaculture using machine learning (LSTM, GRU, CNN). Processes sensor data (pH, turbidity, potability) and provides actionable insights through a web app.
# 🌊 Smart Water Quality Prediction for Aquaculture Using Machine Learning

This **capstone project** focuses on predicting water quality in aquaculture using advanced machine learning techniques. By analyzing water parameters such as **pH**, **turbidity**, and **potability**, this system helps monitor and ensure safe water conditions for aquatic life.  

⚡ The solution leverages **LSTM**, **GRU**, and **CNN models**, and is designed for real-time insights via a simple web app interface (Streamlit / Flask).

---

## 🎯 Project Goals

✅ Predict water potability and quality from sensor data  
✅ Enable aquaculture managers to take action before water quality deteriorates  
✅ Build a modular, scalable, and deployable ML pipeline  

---

## 🛠 Technologies Used

- **Python 3.x**
- **TensorFlow / Keras**
- **scikit-learn**
- **Pandas**, **NumPy**
- **Streamlit** / **Flask** (for the web interface)
- **Matplotlib**, **Seaborn** (for visualizations)

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
🌟 Modular code (easy to extend for new sensors / models)  
🌟 Ready for deployment on cloud or local servers  

---

## 💡 Example Use Cases

- Automated monitoring in aquaculture ponds  
- Early detection of unsuitable water conditions  
- Integration into IoT-based smart aquaculture systems  

---

## 📄 License

This project is licensed under the **MIT License** — free to use and modify with attribution.

---

## 🙌 Acknowledgments

🙏 Thanks to my mentors, peers, and the open-source community that enabled the creation of this project. Special thanks to TensorFlow, Keras, Pandas, and Streamlit contributors.

---

