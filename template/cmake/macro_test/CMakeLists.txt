# set cmake version
cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

# set project information
set(project_name "afa05a6348902c252ae10d48879826b3")
PROJECT(${project_name}
        VERSION 0.0.1
        LANGUAGES CXX
)

# set language standards
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# include template
include_directories()
# lib template
link_directories()

# cmake -DMACRO_TEST=TEST_1 ..
set(MACRO_TEST "TEST" CACHE STRING "describe: this is a test var")
# add code:
#   define TEST
add_definitions(-D${MACRO_TEST})

# cmake -DMACRO_VALUE=VALUE -DMACRO_VALUE_VALUE=10 ..
set(MACRO_VALUE "VALUE" CACHE STRING "describe: this is a test var")
set(MACRO_VALUE_VALUE "" CACHE STRING "describe: this is a test var")
# add code:
#   define VALUE
if (MACRO_VALUE_VALUE STREQUAL "")
    add_definitions(-D${MACRO_VALUE})
else ()
    add_definitions(-D${MACRO_VALUE}=${MACRO_VALUE_VALUE})
endif ()

add_definitions(-DCMAKE_TEST=100)

# add source code file
file(GLOB_RECURSE SRC "${CMAKE_SOURCE_DIR}/main.cpp")
add_executable(${project_name} ${SRC})

# link
target_link_libraries(${project_name})
