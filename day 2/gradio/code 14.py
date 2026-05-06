import gradio as gr


def calculate_total(numbers_text):
    numbers = [int(num.strip()) for num in numbers_text.split(",")]
    total = 0

    for num in numbers:
        total += num

    return total


app = gr.Interface(
    fn=calculate_total,
    inputs=gr.Textbox(
        label="Enter numbers",
        placeholder="Example: 10, 20, 30, 40, 50"
    ),
    outputs=gr.Number(label="Total"),
    title="List Sum Calculator",
    description="Enter numbers separated by commas to calculate their total."
)

app.launch()
