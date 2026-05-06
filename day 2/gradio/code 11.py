import gradio as gr


def calculate_factorial(num):
    num = int(num)

    if num < 0:
        return "Factorial is not defined for negative numbers."

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    return f"Factorial: {factorial}"


app = gr.Interface(
    fn=calculate_factorial,
    inputs=gr.Number(label="Enter a number", precision=0),
    outputs=gr.Textbox(label="Result"),
    title="Factorial Calculator",
    description="Enter a non-negative number to calculate its factorial."
)

app.launch()
