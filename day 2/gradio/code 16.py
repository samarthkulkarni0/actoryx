import gradio as gr
import pandas as pd


def show_first_10_records(file):
    try:
        if file is None:
            return "Please upload a CSV file."

        df = pd.read_csv(file.name)
        return df.head(10)

    except FileNotFoundError:
        return "The specified file was not found."
    except pd.errors.EmptyDataError:
        return "The specified file is empty."
    except pd.errors.ParserError:
        return "Error parsing the CSV file."
    except Exception as e:
        return f"An error occurred: {e}"


app = gr.Interface(
    fn=show_first_10_records,
    inputs=gr.File(label="Upload students.csv file", file_types=[".csv"]),
    outputs=gr.Dataframe(label="First 10 records"),
    title="Student CSV Viewer",
    description="Upload a CSV file to view the first 10 student records."
)

app.launch()
