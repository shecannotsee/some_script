import os
import shutil
from typing import NoReturn
from utils.file import get_content, write_file

def cpp_project_generation() -> NoReturn:
    mock_content: str = get_content(
        os.path.dirname(os.getcwd()),  # ..
        "template",                     # template
        "sys_func_mock.h",              # sys_func_mock.h
    )   # ../template/sys_func_mock.h

    project_name: str = input("Please enter the project name: ")
    generate_path: str = input("Please enter the generation path: ")

    project_path = os.path.join(generate_path, project_name)
    try:
        os.makedirs(project_path, exist_ok=False)
        print(f"Directory: {project_path} has been created.")
    except FileExistsError:
        print(f"Error: Directory: {project_path} already exists.")
        exit(1)

    # copy template to new project
    source_path: str = os.path.join(
        os.path.dirname(os.getcwd()),  # ..
        "template",                     # template
        "cpp_project",                  # cpp_project
    )   # ../template/cpp_project

    # Traverse all files and folders in the source directory
    for item in os.listdir(source_path):
        item_source_path = os.path.join(source_path, item)  # 使用不同的变量
        destination_path = os.path.join(project_path, item)

        # If it is a file, copy the file; If it is a directory, recursively copy
        if os.path.isfile(item_source_path):
            shutil.copy(item_source_path, destination_path)
        elif os.path.isdir(item_source_path):
            shutil.copytree(item_source_path, destination_path)  # Recursively copy directory

    print(f"C++ project generation success to {project_path}")
    print("If you want to generate cmake, please refer to: https://github.com/shecannotsee/cmake_template")
