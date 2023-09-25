import sys
import textwrap

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent(f'''
########################################################################################################################
# Import lib                                                                                                           #
########################################################################################################################

# include
include_directories(${{CMAKE_SOURCE_DIR}}/third_party/googletest-install/include)

# lib
link_directories(${{CMAKE_SOURCE_DIR}}/third_party/googletest-install/lib)

# Internal project
include_directories(${{CMAKE_SOURCE_DIR}}/src)
include_directories(${{CMAKE_SOURCE_DIR}}/test)
include_directories(${{CMAKE_SOURCE_DIR}}/{module_name})

''')

print(code)
