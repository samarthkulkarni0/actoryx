import streamlit as st

st.title("Check Even or Odd")

num = st.number_input("Enter an integer", step=1)

if st.button("Check"):
    if num % 2 == 0:
        st.success("The number is Even")
    else:
        st.success("The number is Odd")