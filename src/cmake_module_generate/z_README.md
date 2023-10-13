## 脚本描述

### 00.py

主要用来调用其他脚本来展示 cmake 代码或者是生成 cmake 相关文件

```bash
~$ python3 00.py

1.simple cmake
2.default cmake,one CMakeLists.txt(include lib,test,exec)
3.modular organization

Please select:3
install path(/home/a):/home/shecannotsee/desktop/temp/cmake_test
generate success.

~$ tree /home/shecannotsee/desktop/temp/cmake_test
/home/shecannotsee/desktop/temp/cmake_test
├── cmake
│   ├── compilation_options.cmake
│   ├── config.cmake
│   ├── import.cmake
│   ├── src_build.cmake
│   ├── target_exec.cmake
│   ├── target_test.cmake
│   └── z_install.cmake
└── CMakeLists.txt

1 directory, 8 files
~$ ......
```

通过 select 选择方法，方法 3 会在设置路径目录下生成相关文件

方法 1 和 2 均是在终端显示简单或者完整的 cmake 代码



### CMakeLists_generate.py

用来生成模块化 cmake 的 CMakeLists.txt

```bash
~$ python3 CMakeLists_generate.py
cmake_minimum_required(VERSION 3.11)

########################################################################################################################
# Project Settings                                                                                                     #
########################################################################################################################

set(project_name "placeholder_name")
PROJECT(${{project_name}}
        VERSION      0.0.1
        LANGUAGES    CXX
        )

# [Release] or [Debug] or [MinSizeRel]
set(compilation_options "Debug")

set(library_static_name "${{project_name}}_static")
set(library_dynamic_name "${{project_name}}_dynamic")

########################################################################################################################
# include                                                                                                              #
########################################################################################################################

include(${CMAKE_SOURCE_DIR}/cmake/compilation_options.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/config.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/import.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/src_build.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/target_exec.cmake )
include(${CMAKE_SOURCE_DIR}/cmake/target_test.cmake)
include(${CMAKE_SOURCE_DIR}/cmake/z_install.cmake)

~$ ......
```



### compilation_options_generate.py

用来生成用于**处理编译条件**的**子 cmake 模块**文件

```bash
~$ python3 compilation_options_generate.py 

########################################################################################################################
# Compilation Options                                                                                                  #
########################################################################################################################

# cpp standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# debug symbol
set(CMAKE_CXX_FLAGS "-g")

# target type
set(CMAKE_BUILD_TYPE ${compilation_options})

~$ ......
```



### config_generate.py

用来生成用于**处理全局配置**的**子 cmake 模块**文件

```bash
~$ python3 config_generate.py
Additional modules name(default exec)：KKKKK  

########################################################################################################################
# Global Settings                                                                                                      #
########################################################################################################################

# src target
set(generate_lib ON)

# test target
set(test_name "${project_name}_test")
set(generate_test ON)

# KKKKK target
set(KKKKK_name "${project_name}_KKKKK")
set(generate_KKKKK ON)


~$ ......
```



### import_generate.py

用来生成用于**处理库导入**的**子 cmake 模块**文件

```bash
~$ python3 import_generate.py 
Additional modules name(default exec)：KKKKK

########################################################################################################################
# Import lib                                                                                                           #
########################################################################################################################

# include
include_directories(${CMAKE_SOURCE_DIR}/third_party/googletest-install/include)

"# lib
link_directories(${CMAKE_SOURCE_DIR}/third_party/googletest-install/lib)

# Internal project
include_directories(${CMAKE_SOURCE_DIR}/src)
include_directories(${CMAKE_SOURCE_DIR}/test)
include_directories(${CMAKE_SOURCE_DIR}/KKKKK)

~$ ......
```



### src_build_generate.py

用来生成用于**处理src目录编译**的**子 cmake 模块**文件

```bash
~$ python3 src_build_generate.py 

########################################################################################################################
# src build                                                                                                            #
########################################################################################################################

# source src
file(GLOB_RECURSE SRC "${CMAKE_SOURCE_DIR}/src/*")
# Exclude specific files
# list(REMOVE_ITEM SRC "${CMAKE_SOURCE_DIR}/src/base64.cpp")

# src dependency
set(src_dependency "-pthread")

# src build to lib
if (generate_lib STREQUAL "ON")
    add_library(${library_static_name} STATIC ${SRC})
    # Rename the generated static library
    set_target_properties(${library_static_name} PROPERTIES OUTPUT_NAME ${project_name})

    add_library(${library_dynamic_name} SHARED ${SRC})
    # Rename the generated dynamic library
    set_target_properties(${library_dynamic_name} PROPERTIES OUTPUT_NAME ${project_name})
else()
    message(STATUS "CMakeLists.txt error:src build error")
endif ()

~$ ......
```



### target_test_generate.py

用来生成用于**处理test构建**的**子 cmake 模块**文件

```bash
~$ python3 target_test_generate.py 

########################################################################################################################
# test target build                                                                                                    #
########################################################################################################################

file(GLOB_RECURSE TEST_SRC "${CMAKE_SOURCE_DIR}/test/*")
# Exclude specific files
# list(REMOVE_ITEM TEST_SRC "${CMAKE_SOURCE_DIR}/test/base.cpp")

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

~$ ......
```



### target_exec_generate.py

用来生成用于**处理exec构建**的**子 cmake 模块**文件

```bash
~$ python3 target_exec_generate.py 
Additional modules name(default exec)：KKKKK

############################################################################################################
# KKKKK target build
############################################################################################################

# KKKKK src
file(GLOB_RECURSE KKKKK_SRC "${CMAKE_SOURCE_DIR}/KKKKK/*")
# Exclude specific files
# list(REMOVE_ITEM KKKKK_SRC "${CMAKE_SOURCE_DIR}/KKKKK/base64.cpp")

# KKKKK dependency
set(KKKKK_dependency "-pthread")

# KKKKK target
if (generate_KKKKK STREQUAL "ON")
    add_executable(${KKKKK_name} ${KKKKK_SRC} ${SRC})
    target_link_libraries(${KKKKK_name} ${lib} ${src_dependency} ${KKKKK_dependency})
else()
    message(STATUS "CMakeLists.txt error: KKKKK target build error")
endif ()

~$ ......
```



### z_install_generate.py

用来生成用于**处理项目install**的**子 cmake 模块**文件

```bash
~$ python3 z_install_generate.py 

########################################################################################################################
# Install module                                                                                                       #
########################################################################################################################

# local debug
set(CMAKE_INSTALL_PREFIX "./")
# Release Code
# set(CMAKE_INSTALL_PREFIX "/")

message(STATUS "The default installation path is ${CMAKE_INSTALL_PREFIX}")
message(STATUS "Please use "make install DESTDIR=./PATH" to set install path")

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

~$ ......
```





