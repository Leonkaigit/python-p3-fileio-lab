import os
from pathlib import Path

def write_file(file_name, file_content):
    
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    file_name = str(file_name) + ".txt" if not str(file_name).endswith(".txt") else str(file_name)


    with open(file_name, "w") as file:
        file.write(file_content)

def append_file(file_name, file_content):
    file_name = str(file_name) + ".txt" if not str(file_name).endswith(".txt") else str(file_name)
    with open(file_name, "a") as file:
        file.write(file_content)

def read_file(file_name):
    file_name = str(file_name) + ".txt" if not str(file_name).endswith(".txt") else str(file_name)

    
    try:
        with open(file_name, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"