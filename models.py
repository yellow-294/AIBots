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
