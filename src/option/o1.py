import os
from typing import NoReturn
from utils.file import get_content


def class_generate() -> NoReturn:
    class_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cpp_class.h",                # cpp_class.h
    )   # ../template/cpp_class.h

    
    class_name: str = input("Please enter the class name: ")
    class_content = class_content.replace("afa05a6348902c252ae10d48879826b3", class_name)

    # output
    print(class_content)

