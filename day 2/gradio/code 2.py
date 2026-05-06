import gradio as gr

def check_voting(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

gr.Interface(fn=check_voting,
             inputs=gr.Number(label="Enter your age"),
             outputs="text").launch()