import json
import glob

# Path to the folder containing JSON files
folder_path = './data/faqgovsg/'

def merge_files(file_list):
    merged_data = {'questionListItems': []}
    
    for file_name in file_list:
        print(file_name)
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
            merged_data['questionListItems'].extend(data['questionListItems'])
            # except Exception as e:
            #     print("error occured")
            #     print(merged_data)
            #     print(e) #tell me what went wrong but also show me the data
        
    return merged_data

# Detecting all JSON files in the folder
files_to_merge = glob.glob(folder_path + '*.json')
# print(f"the name of the files:{files_to_merge}")

# Merging the files
merged_question_list_items = merge_files(files_to_merge)

# To save the merged content into a new file
with open('merged_file.json', 'w', encoding="utf-8") as merged_file:
    json.dump(merged_question_list_items, merged_file, indent=4)

print(f"Files have been merged and saved as 'merged_file.json'")
