from fastapi import FastAPI

app = FastAPI()

@app.get("/quadrado/{num}")
def square(num: int):
    return num ** 2

@app.get("/")
def square(num: int):
    return num ** 2