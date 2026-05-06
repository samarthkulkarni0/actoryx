from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def natural_numbers(n: int):
    return {"numbers": list(range(1, n + 1))}