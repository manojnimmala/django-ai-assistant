import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def ask_ai(prompt):
    response = client.chat.completions.create(
        messages=[
            {
            "role": "system",
            "content": """
            Format all answers using Markdown.

            Use:
            - Headings
            - Bullet points
            - Numbered lists
            - Short paragraphs

            Never return one large paragraph.
            """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return response.choices[0].message.content