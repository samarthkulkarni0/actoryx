from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def find_factors(data: NumberInput):
    if data.num <= 0:
        return {"result": "Please enter a positive number."}
    factors = [i for i in range(1, data.num + 1) if data.num % i == 0]
    return {"factors": factors}
