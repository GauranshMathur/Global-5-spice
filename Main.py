import os
from API_Key import key  # Import the API key from your module
from openai import OpenAI

def fine_tune_model(training_file_path, model_name="gpt-3.5-turbo"):
    # Set the OPENAI_API_KEY environment variable
    os.environ['OPENAI_API_KEY'] = key  # Set the API key

    # Create an instance of the OpenAI client
    client = OpenAI()

    # Upload the training file
    response = client.files.create(
        file=open(training_file_path, "rb"),
        purpose="fine-tune"
    )

    # Extract the file ID from the response
    file_id = response.id  # Access the 'id' attribute

    # Create a fine-tuning job
    client.fine_tuning.jobs.create(
        training_file=file_id,
        model=model_name  # Specify the model name
    )

if __name__ == "__main__":
    # Specify the path to the training file
    training_file_path = "data/test.json"

    # Call the function to initiate fine-tuning
    fine_tune_model(training_file_path)
