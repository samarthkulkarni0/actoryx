from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_number(num: int):
    if num > 0:
        return {"result": "Positive"}
    elif num < 0:
        return {"result": "Negative"}
    return {"result": "Zero"}