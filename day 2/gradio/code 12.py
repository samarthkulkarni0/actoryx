import gradio as gr


def find_factors(num):
    num = int(num)

    if num <= 0:
        return "Please enter a positive number."

    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(str(i))

    return f"Factors of {num} are:\n" + "\n".join(factors)


app = gr.Interface(
    fn=find_factors,
    inputs=gr.Number(label="Enter a number", precision=0),
    outputs=gr.Textbox(label="Factors", lines=10),
    title="Factor Finder",
    description="Enter a positive number to find all its factors."
)

app.launch()
