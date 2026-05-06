import gradio as gr


def print_numbers():
    result = ""

    for i in range(1, 11):
        result += f"{i}\n"

    return result


app = gr.Interface(
    fn=print_numbers,
    inputs=None,
    outputs=gr.Textbox(label="Numbers from 1 to 10", lines=10),
    title="Numbers Printer",
    description="Click Submit to display numbers from 1 to 10."
)

app.launch()
