import sys

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# test target build                                                                                         " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF

code += "# test src" + LF
code += "file(GLOB_RECURSE TEST_SRC \"${CMAKE_SOURCE_DIR}/test/*\")" + LF
code += LF
code += "# Exclude specific files" + LF
code += "# list(REMOVE_ITEM TEST_SRC \"${CMAKE_SOURCE_DIR}/test/base64.cpp\")" + LF
code += LF
code += "# test dependency" + LF
code += "set(test_dependency \"-pthread\"" + LF
code += "                    \"-lgtest\")" + LF
code += "                    \"-lgmock\")" + LF
code += LF
code += "# test target" + LF
code += "if (generate_test STREQUAL \"ON\")" + LF
code += "    add_executable(${test_name} ${TEST_SRC} ${SRC})" + LF
code += "    target_link_libraries(${test_name} ${lib} ${src_dependency} ${test_dependency})" + LF
code += "else()" + LF
code += "    message(STATUS \"CMakeLists.txt error:test target build error\")" + LF
code += "endif ()" + LF
code += LF


code += LF

print(code)
