from fastapi import FastAPI, UploadFile, File
import pandas as pd, io

app = FastAPI()

@app.post("/")
async def read_csv(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(await file.read()))
        return df.to_dict(orient="records")

    except Exception as e:
        return {"error": str(e)}