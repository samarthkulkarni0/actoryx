from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CalcInput(BaseModel):
    num1: float
    num2: float
    operation: str

@app.post("/")
def calculate(data: CalcInput):

    if data.operation == "add":
        result = data.num1 + data.num2

    elif data.operation == "subtract":
        result = data.num1 - data.num2

    elif data.operation == "multiply":
        result = data.num1 * data.num2

    elif data.operation == "divide":
        result = data.num1 / data.num2 if data.num2 != 0 else "Error"

    else:
        result = "Invalid operation"

    return {
        "num1": data.num1,
        "num2": data.num2,
        "operation": data.operation,
        "result": result
    }