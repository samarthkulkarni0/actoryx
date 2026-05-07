from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sum_digits(num: int):
    num = abs(num)
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return {"sum": total}