import gradio as gr


def calculate(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2

    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (cannot divide by zero)"

    return addition, subtraction, multiplication, division


app = gr.Interface(
    fn=calculate,
    inputs=[
        gr.Number(label="Enter first number"),
        gr.Number(label="Enter second number"),
    ],
    outputs=[
        gr.Number(label="Addition"),
        gr.Number(label="Subtraction"),
        gr.Number(label="Multiplication"),
        gr.Textbox(label="Division"),
    ],
    title="Basic Calculator",
    description="Enter two numbers to calculate addition, subtraction, multiplication, and division."
)

app.launch()
