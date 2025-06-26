import os
from pprint import pprint
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

## Moja sprava
user_message = "Spocitaj mi kolko je 100 krat 4"

## System prompt
system_prompt = "Si inteligentny asistent, ktory dokaze vykonavat matematicke vypocty. Ak potrebujes vykonat vypocet, pouzi nastroj 'calculator' vo formate TOOL: calculator(...)."

## LLM call - navrh vypoctu
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
)

assistant_reply = response.choices[0].message.content
print("Assistant reply:", assistant_reply)

## Extrakcia vypoctu z odpovede LLM
import re

match = re.search(r'TOOL:\s*calculator\((.*?)\)', assistant_reply)
if match:
    expression = match.group(1)
    try:
        result = eval(expression)
        print("Vypocet:", expression, "=", result)

        ## Spat do LLM
        followup = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": assistant_reply},
                {"role": "user", "content": f"Vysledok: {result}"}
            ]
        )
        print("Finalna odpoved LLM:", followup.choices[0].message.content)

    except Exception as e:
        print("Chyba:", e)
else:
    print("Ziadny vypocet nie je k dispozicii.")
