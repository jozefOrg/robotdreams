import os
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that tells jokes."},
        {"role": "user", "content": "Hi, tell me a joke"}
    ]
)

pprint(response.choices[0].message.content)

response2 = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that tells jokes."},
        {"role": "user", "content": "Hi, tell me the previous joke"}
    ]
)

pprint(response2.choices[0].message.content)

