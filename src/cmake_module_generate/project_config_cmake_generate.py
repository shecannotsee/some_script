import sys
import textwrap

# 获取命令行参数
project_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional project name：")

code = textwrap.dedent(f"""
# ${{{project_name}_FOUND}}       : right get
# ${{{project_name}_INCLUDE_DIR}} : include
# ${{{project_name}_LIBRARIES}}   : lib
# ${{{project_name}_LINK_TARGET}} : link target

set({project_name} "{project_name}")
set(${{{project_name}}}_FOUND "1")
set(${{{project_name}}}_INCLUDE_DIR   "${{CMAKE_PREFIX_PATH}}/include")
set(${{{project_name}}}_LIBRARIES     "${{CMAKE_PREFIX_PATH}}/lib")
set(${{{project_name}}}_LINK_TARGET   "{project_name}")

""")

print(code)
