
import streamlit as st

st.title("Sign of a Number")

num = st.number_input("Enter a number")

if st.button("Check"):
    if num > 0:
        st.success("Positive")
    elif num < 0:
        st.success("Negative")
    else:
        st.info("Zero")