import gradio as gr

def compare_numbers(num1, num2):
    if num1 > num2:
        return "The first number is greater."
    elif num2 > num1:
        return "The second number is greater."
    else:
        return "Both numbers are equal."

gr.Interface(fn=compare_numbers,
             inputs=[gr.Number(label="First number"),
                     gr.Number(label="Second number")],
             outputs="text").launch()