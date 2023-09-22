import sys

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# Global Settings                                                                                           " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF
code += "# project name" + LF
code += "set(project_name \"project_name\")" + LF
code += LF
code += "# [Release] or [Debug] or [MinSizeRel]" + LF
code += "set(compilation_options \"Debug\")" + LF
code += LF
code += "# src target" + LF
code += "set(library_static_name \"${project_name}_static\")" + LF
code += "set(library_dynamic_name \"${project_name}_dynamic\")" + LF
code += LF
code += "# test target" + LF
code += "set(test_name \"${project_name}_test\")" + LF
code += LF
code += "# exec target" + LF
code += "set(test_name \"${project_name}_exec\")" + LF
code += LF

print(code)
