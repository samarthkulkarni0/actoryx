import streamlit as st

st.title("Arithmetic Operations")

a = st.number_input("Enter first number")
b = st.number_input("Enter second number")

operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):
    
    if operation == "Addition":
        st.write("Result:", a + b)

    elif operation == "Subtraction":
        st.write("Result:", a - b)

    elif operation == "Multiplication":
        st.write("Result:", a * b)

    elif operation == "Division":
        if b != 0:
            st.write("Result:", a / b)
        else:
            st.error("Cannot divide by zero")