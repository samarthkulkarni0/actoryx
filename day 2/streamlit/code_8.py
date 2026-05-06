import streamlit as st

st.title("Multiplication Table")

num = st.number_input("Enter a number", step=1)

if st.button("Generate Table"):
    for i in range(1, 11):
        st.write(f"{num} x {i} = {num * i}")