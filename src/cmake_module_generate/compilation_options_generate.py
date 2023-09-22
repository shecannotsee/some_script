import sys
import textwrap

# 获取命令行参数
# module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

code = textwrap.dedent('''
########################################################################################################################
# Compilation Options                                                                                                  #
########################################################################################################################

# cpp standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# debug symbol
set(CMAKE_CXX_FLAGS "-g")

# target type
set(CMAKE_BUILD_TYPE ${compilation_options})

''')

print(code)
