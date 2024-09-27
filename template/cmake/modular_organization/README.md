# modular_organization

## I. Overall Concept

#### Code and Output

For a C++ project (referred to as cpp_project_template), the essential targets are two sets of outputs consisting of source code and test code.

- src directory and its corresponding output
- test directory and its corresponding output
- Other directories and their corresponding outputs

#### Project Compilation Settings

- Compilation target: Debug or Release, using `CMAKE_BUILD_TYPE`
- Build test module, using `BUILD_TESTS`
- Installation directory, using `CMAKE_INSTALL_PREFIX`
- Path for third-party libraries, using `XXX_ROOT_DIR`

#### C++ Project Settings

- Language standards: C++11, 14, 17, 20 (`-fcoroutines`), etc.
- Compilation commands: `-g`, `-O2`, etc.

## II. Actual Project Structure and Details

### 1. Directory Structure

```bash
$ tree -L 2
.
├── build_1.sh
├── build_2.sh
├── build_3.sh
├── build_gtest.sh
├── cmake
│   ├── build.cmake
│   ├── import_third_party.cmake
│   ├── install.cmake
│   ├── target_src.cmake
│   └── target_test.cmake
├── CMakeLists.txt
├── googletest-1.12.0
│   ├── include
│   └── lib
├── README_CN.md
├── src
│   ├── cal.cpp
│   └── cal.h
└── test
    ├── cal.cpp
    └── main.cpp

6 directories, 15 files
$
```

Here, only CMake-related files and their functions are described.

### 2. CMakeLists.txt

This file mainly handles global build information and preliminary variables, as well as includes sub-files.

1. Global Information: project name, version, language
2. Global Options: whether to build release, whether to build tests, whether to build dynamic libraries
3. Some fixed information that needs to be declared in advance: src directory, src linking variables, test names, test linking variables
4. Includes CMake sub-files in order

For custom additions: To add extra targets, refer to the test module’s handling method, declare the target name and linking variables, then add the corresponding CMake sub-files. If needed, links should also be added in `cmake/import_third_party.cmake` and installation methods in `cmake/install.cmake`.

### 3. cmake Directory

#### (1) build.cmake

This file mainly handles compilation commands and some C++ standards.

1. Language standards: C++ standard settings
2. Compilation instructions: build type, optimization level, and other compilation instructions

For custom additions: To add extra compilation instructions, refer to the template in this file.

#### (2) import_third_party.cmake

This file mainly handles the introduction of third-party libraries.

For custom additions: You can refer to the way gtest is introduced in the test module to introduce other third-party libraries for other targets.

#### (3) target_src.cmake

This file mainly processes the target generation in src. By default, the code in src generates a static library, and a dynamic library can be generated based on global options. There’s also a header list for declaring all .h and .hpp files for easier installation.

For custom additions: This file usually does not need to be changed.

#### (4) target_test.cmake

This file mainly handles the target generation in test and can serve as a sample for constructing other targets.

For custom additions: This file usually does not need to be changed.

#### (5) install.cmake

This file mainly handles installation issues after building the project. It first installs everything in src by default, then selectively installs the dynamic library and test modules based on options.

For custom additions: For additional targets, refer to the target test code sample for installation.

#### (6) Custom File

For an additional target named sample, it needs to first be referenced in CMakeLists.txt similar to target-test to add global information, and then a CMake file named target_sample.cmake should be added in include. Next, dependencies for sample should be added in `cmake/import_third_party.cmake`. Then, handle the build directory and build targets in target_sample.cmake. Finally, add the corresponding installation method in `cmake/install.cmake`.