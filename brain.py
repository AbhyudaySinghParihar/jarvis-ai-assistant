from groq import Groq
from config import GROQ_API_KEY

# Connect to Groq
client = Groq(api_key=GROQ_API_KEY)


def ask_jarvis(question):

    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are Jarvis, a highly intelligent desktop AI assistant. "
                    "Speak naturally in English. "
                    "Be concise and professional. "
                    "Address the user as Sir when appropriate. "
                    "Avoid unnecessarily long answers."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ],

        temperature=0.7,
        max_completion_tokens=500
    )

    return response.choices[0].message.content
