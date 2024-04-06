import json

def create_conversation_data(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    for item in data['questionListItems']:
        user = item['title']
        assistant = item['answer']['body']
        assistant = assistant.replace("<p>", "")
        assistant = assistant.replace("</p>", "")

        conversation = {
            "messages": [
                {"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ]
        }

        with open(output_file, 'a') as f:
            json.dump(conversation, f)
            f.write('\n')  # Add a newline character to separate conversations
    
if __name__ == "__main__":
    input_file = "data/ipos_data_page_1.json"
    output_file = "data/test.json"
    
    create_conversation_data(input_file, output_file)
    print("Conversion completed. Output saved to:", output_file)
