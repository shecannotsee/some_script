# set cmake version
cmake_minimum_required(VERSION 3.10)
set(PROJECT_NAME "afa05a6348902c252ae10d48879826b3")
project(${PROJECT_NAME})

# test
message(STATUS "test start--------------------------------------------------------------------------------------------")

# set var
set(MY_VAR "Hello cmake!")
message(STATUS "MY_VAR:${MY_VAR}")
message(WARNING "warning test:MY_VAR:${MY_VAR}")

# if-elseif-else
set(ERROR_TEST OFF)
if (${ERROR_TEST} STREQUAL ON)
    message(SEND_ERROR "error")
    message(FATAL_ERROR "error")
elseif (${ERROR_TEST} STREQUAL OFF)
    message(STATUS "ERROR_TEST close: ${ERROR_TEST}")
else ()
    message(STATUS "Unknown ERROR_TEST: ${ERROR_TEST}")
endif ()

# function
function(PRINT_MESSAGE message)
    message(STATUS "[PRINT_MESSAGE] ${message}")
endfunction()
PRINT_MESSAGE(${MY_VAR})

# os
if (CMAKE_SYSTEM_NAME STREQUAL "Linux")
    PRINT_MESSAGE("os:linux")
elseif (CMAKE_SYSTEM_NAME STREQUAL "Darwin")
    PRINT_MESSAGE("os:macOS")
elseif (CMAKE_SYSTEM_NAME STREQUAL "Windows")
    PRINT_MESSAGE("os:windows")
else ()
    PRINT_MESSAGE("Unknown os")
endif ()

# compiler
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    PRINT_MESSAGE("compiler:gnu c++")
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
    PRINT_MESSAGE("compiler:clang c++")
elseif (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
    PRINT_MESSAGE("compiler:msvc c++")
else ()
    PRINT_MESSAGE("compiler:Unsupported compiler")
endif ()

# get list
function(PRINT_ITEM message)
    message(STATUS "[PRINT_ITEM] ${message}")
endfunction()
set(MY_LIST 1 2 3 4 5 "-pthread")
foreach(item IN LISTS MY_LIST)
    PRINT_ITEM("item: ${item}")
endforeach()

# test sample: cmake -Dcommand_line_t1=t1 -Dcommand_line_t3=t3 ..
# change var from command line
set(command_line_t1 "1")
set(command_line_t2 "2")
PRINT_MESSAGE("init command_line_t1: ${command_line_t1}")
PRINT_MESSAGE("init command_line_t2: ${command_line_t2}")

set(command_line_t1 "file_default_value" CACHE STRING "describe: this is a test var")
PRINT_MESSAGE("command_line_t1:${command_line_t1}")

if(NOT DEFINED command_line_t3)
    set(command_line_t3 "file_default")
endif()
PRINT_MESSAGE("command_line_t3:${command_line_t3}")

# link lib test
set(link_libs "lib1")
# add: lib2 lib3 lib4
list(APPEND link_libs "lib2" "lib3" "lib4")
list(APPEND link_libs "lib5")
PRINT_MESSAGE("link_libs:${link_libs}")

add_executable(temp main.cpp)
# clang++ -g  main.cpp -o temp -llib1  -llib2  -llib3  -llib4  -llib5
target_link_libraries(temp ${link_libs})


message(STATUS "test done---------------------------------------------------------------------------------------------")
