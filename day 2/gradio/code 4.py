import gradio as gr

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

gr.Interface(fn=check_number,
             inputs=gr.Number(label="Enter number"),
             outputs="text").launch()