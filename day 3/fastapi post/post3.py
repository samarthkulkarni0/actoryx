from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CompareInput(BaseModel):
    num1: int
    num2: int

@app.post("/")
def compare(data: CompareInput):
    if data.num1 > data.num2:
        return {"result": "First number is greater"}
    elif data.num2 > data.num1:
        return {"result": "Second number is greater"}
    else:
        return {"result": "Both are equal"}
