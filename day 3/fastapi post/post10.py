from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def sum_of_digits(data: NumberInput):
    num = abs(data.num)
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits += digit
        num = num // 10
    return {"sum_of_digits": sum_digits}
