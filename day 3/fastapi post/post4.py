from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def check_number(data: NumberInput):
    if data.num > 0:
        return {"result": "Positive"}
    elif data.num < 0:
        return {"result": "Negative"}
    return {"result": "Zero"}
