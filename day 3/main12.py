from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_prime(num: int):
    if num <= 1:
        return {"result": "Not prime"}
    for i in range(2, num):
        if num % i == 0:
            return {"result": "Not prime"}
    return {"result": "Prime"}