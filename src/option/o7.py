import os
from typing import NoReturn
from utils.file import get_content, write_file

def modular_organization_cmake_gen() -> NoReturn:
    CMakeLists_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "modular_organization",       # modular_organization
        "CMakeLists.txt"              # CMakeLists.txt
    )   # ../template/cmake/modular_organization/CMakeLists.txt

    build_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "modular_organization",       # modular_organization
        "cmake",                      # cmake
        "build.cmake"                 # build.cmake
    )   # ../template/cmake/modular_organization/cmake/build.cmake

    import_third_party_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "modular_organization",       # modular_organization
        "cmake",                      # cmake
        "import_third_party.cmake"    # import_third_party.cmake
    )   # ../template/cmake/modular_organization/cmake/import_third_party.cmake

    target_src_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "modular_organization",       # modular_organization
        "cmake",                      # cmake
        "target_src.cmake"            # target_src.cmake
    )   # ../template/cmake/modular_organization/cmake/target_src.cmake

    target_test_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "modular_organization",       # modular_organization
        "cmake",                      # cmake
        "target_test.cmake"           # target_test.cmake
    )   # ../template/cmake/modular_organization/cmake/target_test.cmake

    install_content: str = get_content(
        os.path.dirname(os.getcwd()), # ..
        "template",                   # template
        "cmake",                      # cmake
        "modular_organization",       # modular_organization
        "cmake",                      # cmake
        "install.cmake"               # install.cmake
    )   # ../template/cmake/modular_organization/cmake/install.cmake
    
    # Obtain the generation path
    generate_path: str = str()
    while True:
        generate_path = input("Please enter the generation path:")
        if os.path.isdir(generate_path):
            print(f"The generated directory is: {generate_path}")
            break
        else:
            print("The provided path is not a valid directory, please re-enter.")

    # Generate file: CMakeLists.txt
    file: str = os.path.join(generate_path, "CMakeLists.txt")
    write_file(file, CMakeLists_content)
    # Create the cmake directory and switch to it   
    generate_path: str = os.path.join(generate_path, "cmake")
    os.makedirs(generate_path, exist_ok=True)
    
    # Generate file: cmake/build.cmake
    file: str = os.path.join(generate_path, "build.cmake")
    write_file(file, build_content)

    # Generate file: cmake/import_third_party.cmake
    file: str = os.path.join(generate_path, "import_third_party.cmake")
    write_file(file, import_third_party_content)

    # Generate file: cmake/target_src.cmake
    file: str = os.path.join(generate_path, "target_src.cmake")
    write_file(file, target_src_content)

    # Generate file: cmake/target_test.cmake
    file: str = os.path.join(generate_path, "target_test.cmake")
    write_file(file, target_test_content)

    # Generate file: cmake/install.cmake
    file: str = os.path.join(generate_path, "install.cmake")
    write_file(file, install_content)
