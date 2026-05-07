from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def calculate_factorial(data: NumberInput):
    if data.num < 0:
        return {"result": "Factorial is not defined for negative numbers."}
    factorial = 1
    for i in range(1, data.num + 1):
        factorial *= i
    return {"result": f"Factorial: {factorial}"}
