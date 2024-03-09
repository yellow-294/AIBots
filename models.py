from beanie import Document
from pydantic import BaseModel
from typing import List
from enum import Enum


class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    role: str
    content: str


class Conversation(Document):
    messages: List[Message]


async def insert_message(role, prompt):
    input_tuple = ("role", role), ("content", prompt)
    input_dict = dict(input_tuple)
    msg = Message(**input_dict)
    convo = Conversation(messages=[msg])
    await convo.insert()
