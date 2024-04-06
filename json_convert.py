import json

input_file = "data/ipos_data_page_1.json"
output_file = "data/data.json"

with open(input_file, 'r') as f:
    data = json.load(f)

for item in data['questionListItems']:
    user = item['title']
    assistant = item['answer']['body']
    assistant = assistant.replace("<p>", "")
    assistant = assistant.replace("</p>", "")

    conversation = {
        "messages": [
            {"role": "system", "content": "You are a goverment chatbot that needs to help businesses with finding services"},
            {"role": "user", "content": user},
            {"role": "assistant", "content": assistant}
        ]
    }

    with open(output_file, 'a') as f:
        json.dump(conversation, f)
        f.write('\n')  # Add a newline character to separate conversations
    

  
print("Conversion completed. Output saved to:", output_file)

