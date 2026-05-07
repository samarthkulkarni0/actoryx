from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def print_numbers():
    return {"numbers": list(range(1, 11))}
