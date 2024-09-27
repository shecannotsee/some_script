import os
from typing import NoReturn
from utils.file import get_content

def minimum_cmake_gen() -> NoReturn:
    # get the content from CMakeLists.txt
    CMakeLists_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "minimum_cpp",                # minimum_cpp
        "CMakeLists.txt"              # CMakeLists.txt
    )   # ../template/cmake/minimum_cpp/CMakeLists.txt
    
    # output
    print(CMakeLists_content)
    
