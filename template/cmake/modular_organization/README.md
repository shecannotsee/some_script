# modular_organization

## I. General Concept

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
│   ├── target_other.cmake
│   └── target_test.cmake
├── CMakeLists.txt
├── googletest-1.12.0
│   ├── include
│   └── lib
├── README_CN.md
├── src
│   ├── cal.cpp
│   └── cal.h
├── other
│   └── main.cpp
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

#### (4) target_other.cmake

This file serves as an example of how to add a new target to the project, specifically an executable module. Related code can be found in this file, `CMakeLists.txt`, `(5) target_test.cmake`, and `install.cmake`.

For custom additions: Modify as needed. When adding new targets, ensure you add relevant entries in `CMakeLists.txt`, this file, `(5) target_test.cmake`, and `install.cmake`.

#### (5) target_test.cmake

This file handles the generation of the `test` target and can serve as a sample for building other targets. Note that if other modules use a `main` entry point, you need to exclude the `main` file in the test module.

For custom additions: This file usually does not need to be changed.

#### (6) install.cmake

This file handles the installation of the project after it’s built. It installs all contents of `src` by default, and dynamically installs shared libraries and test modules based on options.

For custom additions: For any added targets, follow the example of the `target_other` code to handle installation.

#### (7) Custom Files

Refer to `(4) target_other.cmake`. For any newly added target named `sample`, add global information in `CMakeLists.txt` as done for `target_other`, create a `target_sample.cmake` file in the `cmake` directory, and declare dependencies in `cmake/import_third_party.cmake`. Then, handle the build directory and target creation in `target_sample.cmake`, and add installation instructions in `cmake/install.cmake`.