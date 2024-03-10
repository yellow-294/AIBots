from fastapi import FastAPI
from models import Conversation, Message, Role
from openai import OpenAI
from models import Conversation, Message
from beanie import init_beanie
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.test, document_models=[Conversation])

# Create


@app.post("/conversation/")
async def create_message(role: str, content: str):
    input_tuple = ("role", role), ("content", content)
    input_dict = dict(input_tuple)
    msg = Message(**input_dict)
    convo = Conversation(messages=[msg])
    await convo.insert()

# Read all


@app.get("/conversations/")
async def read_all_conversations():
    return await Conversation.find_all().to_list()

# Read specific


@app.get("/conversations/{conversation_id}")
async def read_conversation(id: str):
    return await Conversation.get(id)

# Update


@app.put("/conversations/update_role/{conversation_id}")
async def update_conversation_role(id: str, role: str):
    convo = await Conversation.get(id)
    convo.messages[0].role = role
    await convo.save()

# Update


@app.put("/conversations/update_content/{conversation_id}")
async def update_conversation_content(id: str, content: str):
    convo = await Conversation.get(id)
    convo.messages[0].content = content
    await convo.save()


# Delete
@app.delete("/conversations/delete/{conversation_id}")
async def delete_conversation(id: str):
    convo = await Conversation.get(id)
    await convo.delete()


@app.post("/prompts/{prompt}")
async def read_item(prompt: str):
    return {"response": await chat_with_gpt(prompt)}


# @app.on_event("shutdown")
# async def shutdown_event():
    # await Conversation.delete_all()


openai_client = OpenAI(
    api_key="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"
)


async def chat_with_gpt(prompt):

    await create_message(Role.USER, prompt)
    messages = await read_all_conversations()
    message_lst = create_message_list(messages)

    response = get_response(message_lst)
    await create_message(Role.ASSISTANT, response)

    return response


def create_message_list(messages):
    message_lst = []
    for message in messages:
        for message in message.messages:
            # Append the message content to the list
            message_lst.append({
                "role": message.role,
                "content": message.content
            })

    return message_lst


def get_response(message_lst):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_lst
    )
    response = response.choices[0].message.content.strip()

    return response
