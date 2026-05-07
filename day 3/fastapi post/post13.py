from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def check_prime(data: NumberInput):
    if data.num <= 1:
        return {"result": "Not a prime number"}
    count = sum(1 for i in range(1, data.num + 1) if data.num % i == 0)
    return {"result": "Prime number" if count == 2 else "Not a prime number"}
