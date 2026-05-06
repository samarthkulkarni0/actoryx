import streamlit as st

st.title("First 10 Natural Numbers (For Loop)")

if st.button("Show Numbers"):
    for i in range(1, 11):
        st.write(i)