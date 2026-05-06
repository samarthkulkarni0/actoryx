from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def print_numbers():
    return {"numbers": list(range(1, 11))}