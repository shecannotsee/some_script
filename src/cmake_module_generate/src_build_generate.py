import sys

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# src build                                                                                                 " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF

code += "# source src" + LF
code += "file(GLOB_RECURSE SRC \"${CMAKE_SOURCE_DIR}/src/*\")" + LF
code += LF
code += "# Exclude specific files" + LF
code += "# list(REMOVE_ITEM SRC \"${CMAKE_SOURCE_DIR}/src/base64.cpp\")" + LF
code += LF
code += "# src dependency" + LF
code += "set(src_dependency \"-pthread\"" + LF
code += "                   )" + LF
code += LF
code += "# src build to lib" + LF
code += "if (generate_lib STREQUAL \"ON\")" + LF
code += "    add_library(${library_static_name} STATIC ${SRC})" + LF
code += "    # Rename the generated static library" + LF
code += "    set_target_properties(${library_static_name} PROPERTIES OUTPUT_NAME ${project_name})" + LF
code += LF
code += "    add_library(${library_dynamic_name} SHARED ${SRC})" + LF
code += "    # Rename the generated dynamic library" + LF
code += "    set_target_properties(${library_dynamic_name} PROPERTIES OUTPUT_NAME ${project_name})" + LF
code += ""
code += "else()" + LF
code += "    message(STATUS \"CMakeLists.txt error:target error\")" + LF
code += "endif ()" + LF
code += LF


code += LF

print(code)
