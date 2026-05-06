import streamlit as st

st.title("Student Grade Calculator")

name = st.text_input("Enter student name")
maths = st.number_input("Maths Marks")
physics = st.number_input("Physics Marks")
chemistry = st.number_input("Chemistry Marks")

if st.button("Calculate"):
    total = maths + physics + chemistry
    avg = total / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    st.write("Total Marks:", total)
    st.write("Grade:", grade)