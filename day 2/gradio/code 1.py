import gradio as gr

def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

gr.Interface(fn=even_odd,
             inputs=gr.Number(),
             outputs="text").launch()