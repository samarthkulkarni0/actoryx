from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NInput(BaseModel):
    n: int

@app.post("/")
def natural_numbers(data: NInput):
    return {"numbers": list(range(1, data.n + 1))}
