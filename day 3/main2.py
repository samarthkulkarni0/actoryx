from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def check_voting(age: int):
    return {"message": "Eligible" if age >= 18 else "Not Eligible"}