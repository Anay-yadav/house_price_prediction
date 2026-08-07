import streamlit as st
import pandas as pd
import pickle

st.title("🏠 House Price Prediction")

# Load model
import pickle

with open("models/house_price_model.pkl", "rb") as f:
    model = pickle.load(f)

st.write("Enter house details")

area = st.number_input("Living Area (GrLivArea)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")


if st.button("Predict Price"):

    # create empty dataframe with all training features
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model.feature_names_in_
    )

    # put user values in correct columns
    input_data["GrLivArea"] = area
    input_data["BedroomAbvGr"] = bedrooms
    input_data["FullBath"] = bathrooms


    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: ₹ {prediction[0]:,.2f}"
    )