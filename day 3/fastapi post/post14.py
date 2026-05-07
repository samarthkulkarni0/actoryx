from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class NumbersInput(BaseModel):
    numbers: List[int]

@app.post("/")
def calculate_total(data: NumbersInput):
    total = sum(data.numbers)
    return {"total": total}
