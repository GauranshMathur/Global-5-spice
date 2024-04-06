from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:personal::9AxHOg7x",
  messages=[
    {"role": "system", "content": "You are a goverment service bot"},
    {"role": "user", "content": "I am a business owner and i want to create a trademark in singapore. How will i do it"}
  ]
)
print(completion.choices[0].message)