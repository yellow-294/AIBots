from models import Conversation, Message, Role, insert_message
from openai import OpenAI


client = OpenAI(
    api_key="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"
)


async def chat_with_gpt(prompt):
    print(prompt)
    await insert_message(Role.USER, prompt)
    messages = await Conversation.find_all().to_list()
    message_lst = create_message_list(messages)
    print(message_lst)
    response = get_response(message_lst)
    await insert_message(Role.ASSISTANT, response)
    print(response)
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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_lst
    )
    response = response.choices[0].message.content.strip()

    return response
