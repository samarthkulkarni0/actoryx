from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def table(num: int):
    return {"table": [f"{num} x {i} = {num*i}" for i in range(1, 11)]}