import gradio as gr


def calculate_grade(name, maths, physics, chemistry):
    maths = int(maths)
    physics = int(physics)
    chemistry = int(chemistry)

    total = maths + physics + chemistry

    if total >= 270:
        grade = "A"
    elif total >= 240:
        grade = "B"
    elif total >= 180:
        grade = "C"
    else:
        grade = "D"

    return f"Name: {name}\nTotal Marks: {total}\nGrade: {grade}"


app = gr.Interface(
    fn=calculate_grade,
    inputs=[
        gr.Textbox(label="Enter student name"),
        gr.Number(label="Enter Maths marks", precision=0),
        gr.Number(label="Enter Physics marks", precision=0),
        gr.Number(label="Enter Chemistry marks", precision=0),
    ],
    outputs=gr.Textbox(label="Result", lines=3),
    title="Student Grade Calculator",
    description="Enter student details and marks to calculate total marks and grade."
)

app.launch()
