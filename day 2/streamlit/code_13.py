import streamlit as st

st.title("Prime Number Check")

num = st.number_input("Enter a number", step=1)

if st.button("Check"):
    if num < 2:
        st.error("Not a Prime Number")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                st.error("Not a Prime Number")
                break
        else:
            st.success("Prime Number")