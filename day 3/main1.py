from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def even_odd(num: int):
    return {"result": "Even" if num % 2 == 0 else "Odd"}