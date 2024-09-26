import os

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
