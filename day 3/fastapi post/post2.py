from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AgeInput(BaseModel):
    age: int

@app.post("/")
def check_voting(data: AgeInput):
    return {"message": "Eligible" if data.age >= 18 else "Not Eligible"}
