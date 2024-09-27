import os
from typing import NoReturn
from utils.file import get_content

def simple_cmake_gen() -> NoReturn:
    # get the content from CMakeLists.txt
    CMakeLists_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "simple",                     # simple
        "CMakeLists.txt"              # CMakeLists.txt
    )   # ../template/cmake/simple/CMakeLists.txt
    
    # output
    print(CMakeLists_content)
    
