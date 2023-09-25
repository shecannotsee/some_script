import sys
import textwrap

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent(f'''
########################################################################################################################
# Global Settings                                                                                                      #
########################################################################################################################

# project name
set(project_name "placeholder_name")
# [Release] or [Debug] or [MinSizeRel]
set(compilation_options "Debug")

# src target
set(library_static_name "${{project_name}}_static")
set(library_dynamic_name "${{project_name}}_dynamic")
set(generate_lib ON)

# test target
set(test_name "${{project_name}}_test")
set(generate_test ON)

# {module_name} target
set({module_name}_name "${{project_name}}_{module_name}")
set(generate_{module_name} ON)

''')

print(code)
