from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def factorial(num: int):
    if num < 0:
        return {"error": "Negative number"}
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return {"factorial": fact}