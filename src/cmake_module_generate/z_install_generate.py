import sys
import textwrap

# 获取命令行参数
# module_name = sys.argv[1] if len(sys.argv) > 1 else input("Additional modules name(default exec)：")

LF = "\n"
code = ""
code += "############################################################################################################" \
        "############" + LF
code += "# Install module                                                                                            " \
        "           #" + LF
code += "############################################################################################################" \
        "############" + LF

code += textwrap.dedent('''
# local debug
set(CMAKE_INSTALL_PREFIX "./")
# Release Code
# set(CMAKE_INSTALL_PREFIX "/")

message(STATUS "The default installation path is ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Please use \\\"make install DESTDIR=./PATH\\\" to set install path")

# test install
install(TARGETS
        ${test_name} DESTINATION ${PROJECT_NAME}/bin
        )
          
if (library STREQUAL "ON")
    # include install
    install(FILES
            ${CMAKE_SOURCE_DIR}/src/base64.h # source head
            DESTINATION # to
            ${PROJECT_NAME}/include # target dir
            )
    # lib install
    install(TARGETS
            ${library_static_name} ${library_dynamic_name}
            DESTINATION ${PROJECT_NAME}/include
            )
endif ()

''')

print(code)
