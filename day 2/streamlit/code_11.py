import streamlit as st

st.title("Factorial Calculator")

num = st.number_input("Enter a number", step=1)

if st.button("Calculate"):
    fact = 1
    for i in range(1, int(num) + 1):
        fact *= i
    st.success(f"Factorial = {fact}")