from fastapi import FastAPI
from utils import get_response

app = FastAPI()


@app.get("/prompts/{prompt}")
def read_item(prompt: str):
    return {"response": get_response(prompt)}
