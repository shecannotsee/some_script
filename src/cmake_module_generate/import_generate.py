import sys

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# Import lib                                                                                                " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF

code += "# include" + LF
code += "include_directories(${CMAKE_SOURCE_DIR}/third_party/googletest-install/include)" + LF
code += LF
code += "# lib" + LF
code += "link_directories(${CMAKE_SOURCE_DIR}/third_party/googletest-install/lib)" + LF
code += LF
code += "# Internal project" + LF
code += "include_directories(${CMAKE_SOURCE_DIR}/src)" + LF
code += "include_directories(${CMAKE_SOURCE_DIR}/test)" + LF
code += "include_directories(${CMAKE_SOURCE_DIR}/exec)" + LF
code += LF

print(code)
