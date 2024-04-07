import json
import os

input_file = "merged_file.json"
output_file = "data/data.jsonl"


Count = 0 

with open(input_file, 'r') as f:
    data = json.load(f)
    
if os.path.exists(output_file):
# Delete the file
    os.remove(output_file)
    
with open(output_file, 'a') as f:
    

    for item in data['questionListItems']:
        user = item['title']
        assistant = repr(item['answer']['body'])
        assistant = assistant.replace("<p>", "")
        assistant = assistant.replace("</p>", "")
        
        #print(assistant)
        
        if "<" in assistant or "\\" in assistant:
            continue
        
        #print(assistant)
        
        conversation = {
            "messages": [
                {"role": "system", "content": "You are a goverment chatbot that needs to help businesses with finding services"},
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant}
            ]
        }
        
        if Count == 5:
            break
        else:    
            Count = Count + 1
        
        json.dump(conversation, f)
        f.write('\n')  # Add a newline character to separate conversations


  
print("Conversion completed. Output saved to:", output_file)

