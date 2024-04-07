import json
import os

input_file = "data/faqgovsg/skillsfuture_data_page_9.json"
output_file = "data/data.jsonl"


with open(input_file, 'r') as f:
    data = json.load(f)
    
with open(output_file, 'a') as f:
    

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
        
        json.dump(conversation, f)
        f.write('\n')  # Add a newline character to separate conversations


  
print("Conversion completed. Output saved to:", output_file)

