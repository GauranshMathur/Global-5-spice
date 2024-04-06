import openai
import tiktoken
from IPython.display import display, Markdown
 
openai.api_key = "YOUR API KEY"

prompt = """
I am a business owner that wants tp apply for a trademark in singapore how will i do it?
"""

result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a government service bot that needs to recommend services to businesses. You should help the user answer the question"},
        {"role": "user", "content": prompt}
    ],
)

print(result)