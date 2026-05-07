from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TableInput(BaseModel):
    num: int

@app.post("/")
def table(data: TableInput):
    return {"table": [f"{data.num} x {i} = {data.num * i}" for i in range(1, 11)]}
