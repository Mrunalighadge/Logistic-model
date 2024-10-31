# streamlit_app.py
import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open('logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app title
st.title("Titanic Survival Prediction")

# User inputs
pclass = st.selectbox("Passenger Class (1 = First, 2 = Second, 3 = Third)", [1, 2, 3])
age = st.slider("Age", 0, 80, 30)
fare = st.slider("Fare", 0, 500, 100)
sex_female = st.radio("Sex", ["Male", "Female"]) == "Female"
embarked_C = st.radio("Embarked", ["C", "Q", "S"]) == "C"
embarked_Q = st.radio("Embarked", ["C", "Q", "S"]) == "Q"

# Prepare input features
user_data = pd.DataFrame({
    "Pclass": [pclass],
    "Age": [age],
    "Fare": [fare],
    "Sex_female": [1 if sex_female else 0],
    "Embarked_C": [1 if embarked_C else 0],
    "Embarked_Q": [1 if embarked_Q else 0]
})

# Prediction button
if st.button("Predict Survival"):
    prediction = model.predict(user_data)
    if prediction[0] == 1:
        st.write("This passenger would have survived.")
    else:
        st.write("This passenger would not have survived.")