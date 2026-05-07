from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    num: int

@app.post("/")
def even_odd(data: NumberInput):
    return {"result": "Even" if data.num % 2 == 0 else "Odd"}
