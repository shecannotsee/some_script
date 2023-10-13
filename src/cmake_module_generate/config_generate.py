import sys
import textwrap

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent(f'''
########################################################################################################################
# Global Settings                                                                                                      #
########################################################################################################################

# src target
set(generate_lib ON)

# test target
set(test_name "${{project_name}}_test")
set(generate_test ON)

# {module_name} target
set({module_name}_name "${{project_name}}_{module_name}")
set(generate_{module_name} ON)

''')

print(code)
