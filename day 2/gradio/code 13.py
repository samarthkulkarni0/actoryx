import gradio as gr


def check_prime(num):
    num = int(num)
    count = 0

    if num <= 1:
        return "Not a prime number"

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return "Prime number"
    else:
        return "Not a prime number"


app = gr.Interface(
    fn=check_prime,
    inputs=gr.Number(label="Enter a number", precision=0),
    outputs=gr.Textbox(label="Result"),
    title="Prime Number Checker",
    description="Enter a number to check whether it is prime."
)

app.launch()
