import json

input_file = "merged_file.json"
output_file = "gcp_dataset.json"

with open(input_file, 'r') as f:
    data = json.load(f)

for item in data['questionListItems']:
    user = item['title']
    #agency = item['agency']['code']
    answer = item['answer']['body']
    answer = answer.replace("<p>", "")
    answer = answer.replace("</p>", "")

    conversation = {
        "input_text": user,
        #"output_text": agency + ": " + answer
        "output_text": answer

    }
    # for debug
    # print(conversation)
    
    with open(output_file, 'a') as f:
        json.dump(conversation, f)
        f.write('\n')  # Add a newline character to separate conversations
    

  
print("Conversion completed. Output saved to:", output_file)

