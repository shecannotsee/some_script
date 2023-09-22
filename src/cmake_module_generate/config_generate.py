import sys
import textwrap

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

code += textwrap.dedent('''
# project name
set(project_name "project_name")
# [Release] or [Debug] or [MinSizeRel]
set(compilation_options "Debug")

# src target
set(library_static_name "${project_name}_static")"
set(library_dynamic_name "${project_name}_dynamic")"
set(generate_lib ON)"

# test target
set(test_name "${project_name}_test")
set(generate_test ON)

''')
code += "# " + module_name + " target" + LF
code += "set(" + module_name + "_name \"${project_name}_" + module_name + "\")" + LF
code += "set(generate_" + module_name + " ON)" + LF
code += LF

print(code)
