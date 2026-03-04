import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_ai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
