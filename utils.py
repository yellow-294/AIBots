from openai import OpenAI
client = OpenAI(
    api_key="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"
)


def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return response.choices[0].message.content.strip()
