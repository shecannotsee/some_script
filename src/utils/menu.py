import sys
from option.o1 import class_generate
from option.o2 import commit_standard
from option.o3 import cpp_project_generation
from option.o4 import mock_sys_function
from option.o5 import minimum_cmake_gen
from option.o6 import simple_cmake_gen
from option.o7 import modular_organization_cmake_gen

class menu:
    def __init__(self):
        self.options = {
            1: ("Class generation in C++", class_generate),
            2: ("Commit standard", commit_standard),
            3: ("C++ project generation", cpp_project_generation),
            4: ("Mock of system functions", mock_sys_function),
            5: ("Minimum CMake", minimum_cmake_gen),
            6: ("Simple CMake", simple_cmake_gen),
            7: ("Modular Organization CMake", modular_organization_cmake_gen)
        }

    def show_menu(self):
        print()
        for key, (description, _) in self.options.items():
            print(f"{key}. {description}")
        print()

    def select(self):
        method = int(sys.argv[1]) if len(sys.argv) > 1 else int(input("Please select:"))
        if method in self.options:
            description, func = self.options[method]
            if func:
                func()
            else:
                print(f"No method implemented for: {description}")
        else:
            print("Invalid selection.")
