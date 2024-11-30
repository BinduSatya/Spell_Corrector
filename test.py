import os

current_directory = os.getcwd()
file_path = os.path.join(current_directory, "text_data")
path = file_path

for file in os.listdir(path):
    print(f"{path}/{file}")
    with open(f"{path}/{file}", 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
    
