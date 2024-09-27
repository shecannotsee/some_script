# some_script

This project primarily uses Python to handle some automation code generation scripts. When located in the `some_script/src` directory, you can run `python3 main.py` to view the list of generated options.

```bash
.../some_script/src$ python3 main.py 

1. Class generation in C++
2. Commit standard
3. C++ project generation
4. Mock of system functions
5. Minimum CMake
6. Simple CMake
7. Modular Organization CMake

Please select:
```

By entering an option and following the prompts, the corresponding code will be generated.



## Generation Options

### 1. C++ Class Generation

Code will be generated using `some_script/template/cpp_class.h` as a template.

### 2. Commit Standard Display

Code will be generated using `some_script/template/commit_standard.txt` as a template.

### 3. C++ Project Generation

Code will be generated based on the C++ project structure under `some_script/template/cpp_project`, and it will automatically call option 7 to generate modular organization CMake code. This option requires inputting the project name and the generation path. Finally, a directory named after the input project name will be created in the specified path, which will contain a complete C++ project structure.

### 4. Mock Template for System Functions

Code will be generated using `some_script/template/sys_func_mock.h` as a template.

### 5. Minimum CMake Code Generation

Code will be generated using `some_script/template/cmake/minimum_cpp/CMakeLists.txt` as a template.

### 6. Simple CMake Code Generation

Code will be generated using `some_script/template/cmake/simple/CMakeLists.txt` as a template.

### 7. Modular Organization CMake Code Generation

Code will be generated based on the CMake structure under `some_script/template/cmake/modular_organization`. This option requires manually inputting the generation path, after which a CMakeLists.txt file and a cmake directory will be generated in the specified path, followed by the creation of multiple .cmake files within the cmake directory.