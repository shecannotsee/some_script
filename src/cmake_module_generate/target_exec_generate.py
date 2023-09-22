import sys

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("请输入执行模块名称：")

code = (f"""
############################################################################################################
# {module_name} target build
############################################################################################################

# {module_name} src
file(GLOB_RECURSE {module_name}_SRC "${{CMAKE_SOURCE_DIR}}/{module_name}/*")
# Exclude specific files
# list(REMOVE_ITEM {module_name}_SRC "${{CMAKE_SOURCE_DIR}}/{module_name}/base64.cpp")

# {module_name} dependency
set({module_name}_dependency "-pthread")

# {module_name} target
if (generate_{module_name} STREQUAL "ON")
    add_executable(${{{module_name}_name}} ${{{module_name}_SRC}} ${{SRC}})
    target_link_libraries(${{{module_name}_name}} ${{lib}} ${{src_dependency}} ${{{module_name}_dependency}})
else()
    message(STATUS "CMakeLists.txt error: {module_name} target build error")
endif ()

""")

print(code)
