import sys
import textwrap
import subprocess
import os

show1 = textwrap.dedent('''
1.generate framework
''')

# 获取命令行参数
print(show1)
generate_method = sys.argv[1] if len(sys.argv) > 1 else input("Please select:")


def write_file(path, file_name, context):
    file_path_ = os.path.join(path, file_name)
    with open(file_path_, "w") as file_:
        file_.write(context)


if generate_method == "1":
    install_path = sys.argv[1] if len(sys.argv) > 1 else input("install path(/home/a):")
    # src ##############################################################################################################
    os.path.join(install_path, "src")
    os.mkdir(install_path + "/src")
    # placeholder_name.h
    command = ["python3", "src_h_generate.py"]
    src_h = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/src", "placeholder_name.h", src_h)
    # placeholder_name.cpp
    command = ["python3", "src_cpp_generate.py"]
    src_cpp = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/src", "placeholder_name.cpp", src_cpp)

    # test #############################################################################################################
    os.path.join(install_path, "test")
    os.mkdir(install_path + "/test")
    # global_test_set.h
    command = ["python3", "global_test_set_generate.py"]
    global_test_set = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/test", "global_test_set.h", global_test_set)
    # main.cpp
    command = ["python3", "test_main_generate.py"]
    test_main = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/test", "main.cpp", test_main)
    # test_example.h
    command = ["python3", "test_example_generate.py"]
    test_example = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/test", "test_example.h", test_example)

    # exec #############################################################################################################
    os.path.join(install_path, "exec")
    os.mkdir(install_path + "/exec")
    # application.cpp
    command = ["python3", "exec_dir_generate.py"]
    exec_main = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/exec", "application.cpp", exec_main)

    # scripts ##########################################################################################################
    os.path.join(install_path, "scripts")
    os.mkdir(install_path + "/scripts")
    command = ["python3", "scripts_dir_generate.py"]
    scripts_gtest = subprocess.check_output(command, universal_newlines=True, stderr=subprocess.STDOUT)
    write_file(install_path + "/scripts", "googletest-1.12.1_build.sh", scripts_gtest)

    # docs #############################################################################################################
    os.path.join(install_path, "docs")
    os.mkdir(install_path + "/docs")
    write_file(install_path + "/docs", "placeholder", "")
    # resource #########################################################################################################
    os.path.join(install_path, "resource")
    os.mkdir(install_path + "/resource")
    write_file(install_path + "/resource", "placeholder", "")
    # docs #############################################################################################################
    write_file(install_path, "README.md", "")

    print("generate success.")
else:
    print("??????")
    exit(1)
