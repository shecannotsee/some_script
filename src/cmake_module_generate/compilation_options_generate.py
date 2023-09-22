import sys

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# Compilation Options                                                                                       " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF
code += "# cpp standard" + LF
code += "set(CMAKE_CXX_STANDARD 11)" + LF
code += "set(CMAKE_CXX_STANDARD_REQUIRED ON)" + LF
code += ""
code += "# debug symbol" + LF
code += "set(CMAKE_CXX_FLAGS \"-g\")" + LF
code += LF
code += "# target" + LF
code += "set(CMAKE_BUILD_TYPE ${compilation_options})" + LF
code += LF


print(code)
