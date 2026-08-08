import streamlit as st
import pandas as pd
import pickle

st.title("🏠 House Price Prediction")

st.write("Enter the house details below to predict the price.")

# Load trained model
with open("models/house_price_model.pkl", "rb") as f:
    model = pickle.load(f)


# -----------------------------
# HOUSE DETAILS
# -----------------------------

st.header("🏠 House Details")

area = st.number_input(
    "Living Area (GrLivArea)",
    min_value=0,
    value=1500
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=0,
    max_value=10,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=0,
    max_value=10,
    value=2
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2015
)

overall_quality = st.number_input(
    "Overall Quality (1-10)",
    min_value=1,
    max_value=10,
    value=5
)

garage_cars = st.number_input(
    "Garage Capacity (Cars)",
    min_value=0,
    max_value=5,
    value=2
)

garage_area = st.number_input(
    "Garage Area (sq ft)",
    min_value=0,
    value=500
)

basement_area = st.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    value=500
)

first_floor = st.number_input(
    "1st Floor Area (sq ft)",
    min_value=0,
    value=1000
)

second_floor = st.number_input(
    "2nd Floor Area (sq ft)",
    min_value=0,
    value=500
)


# -----------------------------
# PREDICTION
# -----------------------------

if st.button("🔮 Predict Price"):

    # Create dataframe with exactly the
    # same features used during training
    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=model.feature_names_in_
    )

    # Put user values into correct columns
    input_data["GrLivArea"] = area
    input_data["BedroomAbvGr"] = bedrooms
    input_data["FullBath"] = bathrooms
    input_data["YearBuilt"] = year_built
    input_data["OverallQual"] = overall_quality
    input_data["GarageCars"] = garage_cars
    input_data["GarageArea"] = garage_area
    input_data["TotalBsmtSF"] = basement_area
    input_data["1stFlrSF"] = first_floor
    input_data["2ndFlrSF"] = second_floor

    # Prediction
    prediction = model.predict(input_data)

    st.success(
        f"🏠 Predicted House Price: ₹ {prediction[0]:,.2f}"
    )