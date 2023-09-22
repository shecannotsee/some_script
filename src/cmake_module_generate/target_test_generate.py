import sys
import textwrap

# 获取命令行参数
# class_name = sys.argv[1] if len(sys.argv) > 1 else input("input class name：")

code = textwrap.dedent('''
########################################################################################################################
# test target build                                                                                                    #
########################################################################################################################

file(GLOB_RECURSE TEST_SRC "${CMAKE_SOURCE_DIR}/test/*")
# Exclude specific files
# list(REMOVE_ITEM TEST_SRC "${CMAKE_SOURCE_DIR}/test/base64.cpp")

# test dependency
set(test_dependency "-pthread"
                    "-lgtest"
                    "-lgmock" )

# test target
if (generate_test STREQUAL "ON")
    add_executable(${test_name} ${TEST_SRC} ${SRC})
    target_link_libraries(${test_name} ${src_dependency} ${test_dependency})
else()
    message(STATUS "CMakeLists.txt error:test target build error")
endif ()

''')

print(code)
