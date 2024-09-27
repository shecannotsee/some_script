# set cmake version
cmake_minimum_required(VERSION 3.10 FATAL_ERROR)

# set project information
set(project_name "afa05a6348902c252ae10d48879826b3")
PROJECT(${project_name}
        VERSION 0.0.1
        LANGUAGES C
)

# set language standards
set(CMAKE_C_STANDARD 99)
set(CMAKE_C_STANDARD_REQUIRED ON)

# include template
include_directories()
# lib template
link_directories()

# add source code file
file(GLOB_RECURSE SRC "${CMAKE_SOURCE_DIR}/main.c")
add_executable(${project_name} ${SRC})

# link
target_link_libraries(${project_name} "-pthread")
