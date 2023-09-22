import sys
import textwrap
import subprocess
import os

show1 = textwrap.dedent('''
1.simple cmake
2.default cmake,one CMakeLists.txt(include lib,test,exec)
3.modular organization
4.common cmake files generate
''')

# 获取命令行参数
print(show1)
generate_method = sys.argv[1] if len(sys.argv) > 1 else input("Please select:")

def write_file(path, file_name, context):
    file_path_ = os.path.join(path, file_name)
    with open(file_path_, "w") as file_:
        file_.write(context)


if generate_method == "1":
    simple_cmake = textwrap.dedent('''
########################################################################################################################
cmake_minimum_required(VERSION 3.10)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(PROJECT_NAME "xxxxx")
set(CMAKE_CXX_FLAGS "-g")# 断点无效处理方案
project(${PROJECT_NAME})

# 目录获取
get_filename_component(sheTestcode_path ${CMAKE_SOURCE_DIR} DIRECTORY)
message(STATUS "sheTestcode_path's path:${sheTestcode_path}")

# include
include_directories()
# lib
link_directories()

file(GLOB_RECURSE SRC "${CMAKE_SOURCE_DIR}/main.cpp")
add_executable(${PROJECT_NAME} ${SRC})

# 链接库
target_link_libraries(${PROJECT_NAME} "-pthread")

########################################################################################################################
    ''')
    print(simple_cmake)
elif generate_method == "2":
    default_cmake = ""
    # compilation_options_generate
    command = ["python3", "compilation_options_generate.py"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    # config_generate
    command = ["python3", "config_generate.py", "exec"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    # import_generate
    command = ["python3", "import_generate.py", "exec"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    # src_build_generate
    command = ["python3", "src_build_generate.py"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    # target_test_generate
    command = ["python3", "target_test_generate.py"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    # target_exec_generate
    command = ["python3", "target_exec_generate.py", "exec"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    # z_install_generate
    command = ["python3", "z_install_generate.py"]
    default_cmake += subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)

    display = textwrap.dedent(f'''
########################################################################################################################
{default_cmake}
########################################################################################################################
    ''')
    print(display)
elif generate_method == "3":
    install_path = sys.argv[1] if len(sys.argv) > 1 else input("install path(/home/a):")
    # CMakeLists_generate
    command = ["python3", "CMakeLists_generate.py"]
    CMakeLists_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "CMakeLists.txt", CMakeLists_context)

    install_path = install_path + "/cmake"
    os.makedirs(install_path, exist_ok=True)
    # compilation_options_generate
    command = ["python3", "compilation_options_generate.py"]
    compilation_options_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "compilation_options.cmake", compilation_options_context)

    # config_generate
    command = ["python3", "config_generate.py", "exec"]
    config_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "config.cmake", config_context)

    # import_generate
    command = ["python3", "import_generate.py", "exec"]
    import_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "import.cmake", import_context)

    # src_build_generate
    command = ["python3", "src_build_generate.py"]
    src_build_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "src_build.cmake", src_build_context)

    # target_test_generate
    command = ["python3", "target_test_generate.py"]
    target_test_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "target_test.cmake", target_test_context)

    # target_exec_generate
    command = ["python3", "target_exec_generate.py", "exec"]
    target_exec_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "target_exec.cmake", target_exec_context)

    # z_install_generate
    command = ["python3", "z_install_generate.py"]
    z_install_context = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path, "z_install.cmake", z_install_context)

    print("generate success.")
elif generate_method == "4":
    command = ["python3", "./common_cmake_file_generate/cmake_file_generate.py"]
    common_make = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    print(common_make)
else:
    print("??????")
    exit(1)
