import streamlit as st
import pandas as pd

st.title("Prediksi Asuransi")

file = st.file_uploader("Upload file CSV")

if file is not None:
    df = pd.read_csv(file)
    st.write("Data:")
    st.write(df.head())
