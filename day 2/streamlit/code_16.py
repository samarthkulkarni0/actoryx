import streamlit as st
import pandas as pd

st.title("Read CSV File")

file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write("First 10 Records:")
    st.dataframe(df.head(10))