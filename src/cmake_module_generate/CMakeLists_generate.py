import sys

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")
LF = "\n"
code = ""
code += "cmake_minimum_required(VERSION 3.11)" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/compilation_options.cmake)" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/config.cmake)" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/import.cmake)" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/src_build.cmake)" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/target_exec.cmake )" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/target_test.cmake)" + LF
code += "include(${CMAKE_SOURCE_DIR}/cmake/z_install.cmake)" + LF
code += "" + LF
code += "PROJECT(${project_name}" + LF
code += "    VERSION      0.0.1" + LF
code += "    LANGUAGES    CXX" + LF
code += ")" + LF



print(code)
