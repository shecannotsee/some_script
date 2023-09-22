import sys
import textwrap

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# Import lib                                                                                                " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF

code += textwrap.dedent('''
# include
include_directories(${CMAKE_SOURCE_DIR}/third_party/googletest-install/include)

"# lib
link_directories(${CMAKE_SOURCE_DIR}/third_party/googletest-install/lib)

# Internal project
include_directories(${CMAKE_SOURCE_DIR}/src)
include_directories(${CMAKE_SOURCE_DIR}/test)
''')
code += "include_directories(${CMAKE_SOURCE_DIR}/" + module_name + ")" + LF
code += LF

print(code)
