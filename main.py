from fastapi import FastAPI
from utils import chat_with_gpt
from models import Conversation, Message
from beanie import init_beanie
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(client.test, document_models=[Conversation])


@app.get("/prompts/{prompt}")
async def read_item(prompt: str):
    return {"response": await chat_with_gpt(prompt)}


@app.on_event("shutdown")
async def shutdown_event():
    await Conversation.delete_all()
