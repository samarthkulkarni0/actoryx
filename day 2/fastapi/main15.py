from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def read_csv():
    try:
        df = pd.read_csv("students.csv")
        return df.head(10).to_dict()

    except FileNotFoundError:
        return {"error": "File not found"}

    except Exception as e:
        return {"error": str(e)}