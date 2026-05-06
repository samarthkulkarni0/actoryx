from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def calculate(num1: float, num2: float):
    return {
        "addition": num1 + num2,
        "subtraction": num1 - num2,
        "multiplication": num1 * num2,
        "division": num1 / num2 if num2 != 0 else "Error"
    }