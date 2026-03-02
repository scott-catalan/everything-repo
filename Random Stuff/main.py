'''
# Project Creation Date: 8:49:20 PM, 2/27/2026
'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "holy shit it works"}

@app.get("/calculate/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"result": num1 + num2}