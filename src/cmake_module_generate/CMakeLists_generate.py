import sys
import textwrap

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

code = textwrap.dedent('''
cmake_minimum_required(VERSION 3.11)
include(${CMAKE_SOURCE_DIR}/cmake/compilation_options.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/config.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/import.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/src_build.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/target_exec.cmake )
include(${CMAKE_SOURCE_DIR}/cmake/target_test.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/z_install.cmake)

PROJECT(${project_name}
    VERSION      0.0.1
    LANGUAGES    CXX
)

''')

print(code)
