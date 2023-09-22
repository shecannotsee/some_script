import sys

# 获取命令行参数
module_name = sys.argv[1] if len(sys.argv) > 1 else input("input exec module name：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# " + module_name + " target build " + LF
code += "############################################################################################################" \
        "############" + LF

code += "# " + module_name + " src" + LF
code += "file(GLOB_RECURSE " + module_name + "_SRC \"${CMAKE_SOURCE_DIR}/" + module_name + "/*\")" + LF
code += LF
code += "# Exclude specific files" + LF
code += "# list(REMOVE_ITEM " + module_name + "_SRC \"${CMAKE_SOURCE_DIR}/" + module_name + "/base64.cpp\")" + LF
code += LF
code += "# " + module_name + " dependency" + LF
code += "set(" + module_name + "_dependency \"-pthread\"" + LF
code += "                      )" + LF
code += LF
code += "# " + module_name + " target" + LF
code += "if (generate_" + module_name + " STREQUAL \"ON\")" + LF
code += "    add_executable(${" + module_name + "_name} ${" + module_name + "_SRC} ${SRC})" + LF
code += "    target_link_libraries(${" + module_name + "_name} ${lib} ${src_dependency} ${" + module_name + "_dependency})" + LF
code += "else()" + LF
code += "    message(STATUS \"CMakeLists.txt error:" + module_name + " target build error\")" + LF
code += "endif ()" + LF
code += LF


code += LF

print(code)
