import gradio as gr


def sum_of_digits(num):
    num = abs(int(num))
    sum_digits = 0

    while num > 0:
        digit = num % 10
        sum_digits += digit
        num = num // 10

    return sum_digits


app = gr.Interface(
    fn=sum_of_digits,
    inputs=gr.Number(label="Enter a number", precision=0),
    outputs=gr.Number(label="Sum of digits"),
    title="Sum of Digits Calculator",
    description="Enter a number to calculate the sum of its digits."
)

app.launch()
