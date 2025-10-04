import streamlit as st
import joblib
import numpy as np

st.title("CTG Guardian")
st.write("Upload CTG features to classify fetal health")

model = joblib.load('model/ctg_model.pkl')

input_data = st.text_input("Enter comma-separated CTG features:")
if input_data:
    try:
        features = np.array([float(x) for x in input_data.split(',')]).reshape(1, -1)
        prediction = model.predict(features)[0]
        label = {1: "Normal", 2: "Suspect", 3: "Pathologic"}[prediction]
        st.success(f"Prediction: {label}")
    except:
        st.error("Invalid input. Please enter 21 numeric values separated by commas.")
