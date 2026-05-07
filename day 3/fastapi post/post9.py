from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def sum_digits(data: NumberInput):
    num = abs(data.num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return {"sum": total}
