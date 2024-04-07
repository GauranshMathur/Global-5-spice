from openai import OpenAI
from API_Key import key
import os

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = key
temperature = 0.1

# Initialize OpenAI client
client = OpenAI()

# Create chat completion request
completion = client.chat.completions.create(
    model="ft:gpt-3.5-turbo-1106:personal::9BDd4X7m",
    messages=[
        {"role": "system", "content": "You are a government service bot"},
        {"role": "user", "content": "I am a business owner and I want to create a trademark in Singapore. How will I do it?"}
    ],
    temperature=temperature
)

# Extracting the response and confidence
response = completion.choices[0].message.content
#confidence = completion.choices[0].message.get('confidence', 1)

print("Response :", response)
#if confidence >= 0.6:
    #print("Response:", response)
#else:
    #print("Due to low confidence, I am unable to provide a response.")
