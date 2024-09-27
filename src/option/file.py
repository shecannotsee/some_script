import os
from typing import NoReturn

def get_content(*path) -> str:
    file_path: str = os.path.join(*path)

    content: str = str()
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(str(e))
        exit(1)
    
    return content

def write_file(path: str, content: str) -> NoReturn:
    with open(path, 'w') as file:
        file.write(content)
        file.write("\n")
