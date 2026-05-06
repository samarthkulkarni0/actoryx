import gradio as gr


def multiplication_table(num):
    num = int(num)
    result = ""

    for i in range(1, 11):
        result += f"{num} x {i} = {num * i}\n"

    return result


app = gr.Interface(
    fn=multiplication_table,
    inputs=gr.Number(label="Enter a number", precision=0),
    outputs=gr.Textbox(label="Multiplication Table", lines=10),
    title="Multiplication Table Generator"
)

app.launch()
