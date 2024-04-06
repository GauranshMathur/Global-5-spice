from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:personal::9AxHOg7x",
  messages=[
    {"role": "system", "content": "You are a goverment service bot"},
    {"role": "user", "content": "How can I trademark my business?"}
  ]
)
print(completion.choices[0].message)