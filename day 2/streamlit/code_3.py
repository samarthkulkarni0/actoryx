import streamlit as st

st.title("Greatest of Two Numbers")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

if st.button("Compare"):
    if a > b:
        st.success("First number is greater")
    elif b > a:
        st.success("Second number is greater")
    else:
        st.success("Both are equal")