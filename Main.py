import os
from API_Key import key  # Import the API key from your module
from openai import OpenAI

# Set the OPENAI_API_KEY environment variable
os.environ['OPENAI_API_KEY'] = key  # Set the API key

# Create an instance of the OpenAI client
client = OpenAI()

# Specify the path to the training file
training_file_path = "data/data.json"

# Specify the model name
model_name = "gpt-3.5-turbo"  # Using the GPT-3.5 Turbo model

# Create a fine-tuning job
client.fine_tuning.jobs.create(
    training_file=training_file_path,
    model=model_name
)
