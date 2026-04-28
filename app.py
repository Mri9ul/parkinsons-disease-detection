import streamlit as st
import pandas as pd
import pickle

# Load model and scaler
with open("parkinsons_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.set_page_config(
    page_title="Parkinson's Disease Detection",
    page_icon="🧠"
)

st.title("🧠 Parkinson's Disease Detection")
st.warning(
    "This app is for educational purposes only and should not be used for real medical diagnosis."
)

st.write(
    "Upload a CSV file containing biomedical voice features. "
    "The model will predict whether Parkinson's disease is detected or not."
)

expected_columns = [
    "MDVP:Fo(Hz)",
    "MDVP:Fhi(Hz)",
    "MDVP:Flo(Hz)",
    "MDVP:Jitter(%)",
    "MDVP:Jitter(Abs)",
    "MDVP:RAP",
    "MDVP:PPQ",
    "Jitter:DDP",
    "MDVP:Shimmer",
    "MDVP:Shimmer(dB)",
    "Shimmer:APQ3",
    "Shimmer:APQ5",
    "MDVP:APQ",
    "Shimmer:DDA",
    "NHR",
    "HNR",
    "RPDE",
    "DFA",
    "spread1",
    "spread2",
    "D2",
    "PPE"
]

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data Preview")
    st.dataframe(data.head())

    # Remove non-feature columns if present
    if "name" in data.columns:
        data = data.drop(columns=["name"])

    if "status" in data.columns:
        data = data.drop(columns=["status"])

    missing_columns = [col for col in expected_columns if col not in data.columns]

    if missing_columns:
        st.error("The uploaded CSV is missing required columns:")
        st.write(missing_columns)
    else:
        input_data = data[expected_columns]

        input_scaled = scaler.transform(input_data)

        predictions = model.predict(input_scaled)

        result_labels = [
            "Parkinson's Disease Detected" if pred == 1 else "No Parkinson's Disease Detected"
            for pred in predictions
        ]

        result_df = data.copy()
        result_df["Prediction"] = result_labels

        st.subheader("Prediction Results")
        st.dataframe(result_df)

        csv = result_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Predictions as CSV",
            data=csv,
            file_name="parkinsons_predictions.csv",
            mime="text/csv"
        )