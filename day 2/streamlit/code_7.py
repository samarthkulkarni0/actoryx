import streamlit as st

st.title("First N Natural Numbers (While Loop)")

n = st.number_input("Enter N", step=1)

if st.button("Show Numbers"):
    i = 1
    while i <= n:
        st.write(i)
        i += 1