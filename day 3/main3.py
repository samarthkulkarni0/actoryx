from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def compare(num1: int, num2: int):
    if num1 > num2:
        return {"result": "First number is greater"}
    elif num2 > num1:
        return {"result": "Second number is greater"}
    else:
        return {"result": "Both are equal"}