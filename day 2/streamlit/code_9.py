import streamlit as st

st.title("Multiplication Table of 9")

if st.button("Show Table"):
    for i in range(1, 11):
        st.write(f"9 x {i} = {9 * i}")