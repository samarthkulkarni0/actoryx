from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def find_factors(num: int):
    return {"factors": [i for i in range(1, num + 1) if num % i == 0]}