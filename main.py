""" This is the main file for the FastAPI application """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    This is the root path of the API
    """
    return {"Hello": "World"}
