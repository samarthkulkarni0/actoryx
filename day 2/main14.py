from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def grade(name: str, maths: int, physics: int, chemistry: int):
    total = maths + physics + chemistry

    if total >= 270:
        grade = "A"
    elif total >= 240:
        grade = "B"
    elif total >= 180:
        grade = "C", "Fail"
    else:
        grade = "D", "Fail"

    return {"name": name, "total": total, "grade": grade}
