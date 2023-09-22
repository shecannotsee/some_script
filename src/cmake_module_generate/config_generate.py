import sys

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

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
code += "set(generate_lib ON)" + LF
code += LF
code += "# test target" + LF
code += "set(test_name \"${project_name}_test\")" + LF
code += "set(generate_test ON)" + LF
code += LF
code += "# " + module_name + " target" + LF
code += "set(" + module_name + "_name \"${project_name}_" + module_name + "\")" + LF
code += "set(generate_" + module_name + " ON)" + LF
code += LF

print(code)
