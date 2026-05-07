from fastapi import FastAPI

app = FastAPI()

@app.post("/")
def sum_list(numbers: str):
    nums = [int(x.strip()) for x in numbers.split(",")]
    return {"total": sum(nums)}
