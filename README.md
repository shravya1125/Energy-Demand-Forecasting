# ⚡ Energy Demand Forecasting (AEP)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) 
![Streamlit](https://img.shields.io/badge/Streamlit-App-red) 
![License](https://img.shields.io/badge/License-MIT-green)

This project was developed under the theme **Sustainable Energy & Efficiency**.  
It forecasts **next-hour electricity demand** using **Machine Learning (Random Forest, LSTM)** and provides an **interactive Streamlit web app** for real-time testing.

---

## 🔑 Features
- Energy demand forecasting using **historical hourly consumption data**.  
- **Random Forest** for fast, interpretable predictions.  
- **LSTM (Deep Learning)** for capturing long-term temporal trends.  
- **Streamlit Web App** for interactive inputs and outputs.  
- **Plotly Visualizations** with annotated prediction points.  
- Trained artifacts (`scaler`, `model`) saved using `joblib` for reusability.  

---

## 📂 Project Structure
📦 Energy-Forecasting  
├── artifacts/ # Saved models & scalers   
│ ├── scaler.joblib   
│ └── random_forest.joblib   
├── AEP_hourly.csv # Dataset (Hourly electricity demand)  
├── energy_demand_forecasting_pjm_aep.ipynb # Jupyter Notebook (model training)  
├── app.py # Streamlit web application  
├── requirements.txt # Dependencies  
└── README.md # Project documentation  

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/Energy-Forecasting.git
cd Energy-Forecasting
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv  
source venv/bin/activate   # On Mac/Linux  
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```  

App will open in your browser at http://localhost:8501.  

## 🗂️ Dataset

We used the AEP_hourly.csv dataset from UCI / PJM Interconnection.  
- Datetime: Hourly timestamp  
- AEP_MW: Energy consumption in MW  

## 🚀 Usage  

1. The app auto-fills the last 8 hours of data from the dataset.  
2. User can adjust any of these values (simulate demand changes).  
3. Click Predict Next Hour Energy to see forecast.  
4. Output:  
- Green box with next-hour predicted MW  
- Plotly chart (Past 24h + Predicted next hour marked in red)

## 📊 Results  

- Random Forest RMSE: ~9222 MW  
- MAPE: ~59%  
- Predictions align with short-term demand trends.

## 🖼️ Screenshots
Web App (Prediction Screen)   
<img width="1366" height="768" alt="Screenshot (140)" src="https://github.com/user-attachments/assets/bb021e22-8e31-4cf8-ad96-7ef24b6a4abe" />


## 🔮 Future Work  
- Integrate real-time IoT energy data from smart meters.  
- Extend to multi-hour forecasting (next 24h).  
- Deploy app on Streamlit Cloud / Heroku.  
- Improve LSTM tuning for better accuracy.

## 📜 License

This project is licensed under the MIT License.  

✍️ Author- Shreya Sati


