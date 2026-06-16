import os
from dotenv import load_dotenv
from groq import Groq



client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def ask_ai(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return response.choices[0].message.content)