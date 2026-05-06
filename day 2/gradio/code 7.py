import gradio as gr

def natural_numbers(n):
    i = 1
    result = []
    while i <= n:
        result.append(i)
        i += 1
    return result

gr.Interface(fn=natural_numbers,
             inputs=gr.Number(label="Enter n"),
             outputs="text").launch()