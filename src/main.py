import os
from utils.menu import menu

if __name__ == "__main__":
    current_path: str = "src"
    if os.path.basename(os.getcwd()) != current_path:
        print(f"Please ensure that the current running directory is located under: {current_path}")
        exit(1)

    cmake_gen: menu = menu()
    cmake_gen.show_menu()
    cmake_gen.select()
