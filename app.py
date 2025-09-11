import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

scaler = joblib.load('./artifacts/scaler.joblib')
rf_model = joblib.load('./artifacts/random_forest.joblib')

# Streamlit UI
st.set_page_config(page_title="Energy Forecasting", layout="wide")
st.title(" Energy Demand Forecasting (AEP)")

st.markdown("""
This interactive app predicts the **next hour energy demand** using a trained Random Forest model and LSTM model for forecasting..

- Last 8 hours are auto-filled from dataset.  
- You can **adjust any value** to test predictions.  
- Hover over the chart to see exact energy values.
""")

# Load dataset
df = pd.read_csv("AEP_hourly.csv", parse_dates=['Datetime'])
df.rename(columns={'Datetime':'timestamp','AEP_MW':'energy'}, inplace=True)
df = df.sort_values('timestamp').reset_index(drop=True)

# Parameters
hours_input = 8   
hours_display = 24 

last_24 = df['energy'].values[-hours_display:]
last_8 = df['energy'].values[-hours_input:]

st.subheader(f" Last {hours_display} hours of energy (MW)")


fig = go.Figure()
fig.add_trace(go.Scatter(
    y=last_24, x=list(range(-hours_display+1,1)), 
    mode='lines+markers', name='Past 24 Hours', line=dict(color='blue')
))
fig.update_layout(
    xaxis_title='Hour', yaxis_title='Energy (MW)',
    title='Energy Consumption (Past 24 Hours)',
    template='plotly_white'
)
st.plotly_chart(fig, use_container_width=True)

st.subheader(" Enter past energy values for prediction (MW)")
energy_inputs = []
cols = st.columns(hours_input)
for i, col in enumerate(cols):
    val = col.number_input(
        f"Hour -{hours_input-i}", 
        value=float(last_8[i]), step=10.0, format="%.2f"
    )
    energy_inputs.append(val)

if st.button("Predict Next Hour Energy"):
    X = np.array(energy_inputs).reshape(1, -1)
    X_scaled = scaler.transform(X)
    pred = rf_model.predict(X_scaled)
    
    st.subheader(" Prediction")
    st.success(f"Predicted next hour energy: {pred[0]:.2f} MW")
    
    # Add predicted point to Plotly chart
    fig.add_trace(go.Scatter(
        y=[pred[0]], x=[1], mode='markers+text', name='Predicted Next Hour',
        marker=dict(color='red', size=12), text=["Predicted"], textposition="top center"
    ))
    fig.update_layout(title='Energy Forecast (Past 24h + Next Hour Prediction)')
    st.plotly_chart(fig, use_container_width=True)
