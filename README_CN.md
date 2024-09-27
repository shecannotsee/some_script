# some_script

该项目主要使用python来处理一些自动化代码生成脚本。当位于`some_script/src`目录下可以使用`python3 main.py`查看可生成列表。

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

通过输入选项, 然后按照提示会生成对应的代码。



## 生成选项

### 1.c++ 类生成

以`some_script/template/cpp_class.h`为模板进行代码生成。

### 2.提交规范展示

以`some_script/template/commit_standard.txt`为模板进行代码生成。

### 3.c++项目生成

以`some_script/template/cpp_project`下的 c++ 项目结构为模板进行代码生成, 并且会调用选项7自动生成模块化组织 cmake 代码。该选项需要输入生成的项目名, 以及生成路径; 最后在生成路径下会生成一个以输入项目名为名称的目录, 该目录是一个完成的 c++ 项目结构。

### 4.系统函数的 mock 模板

以`some_script/template/sys_func_mock.h`为模板进行代码生成。

### 5.最小的 cmake 代码生成

以`some_script/template/cmake/minimum_cpp/CMakeLists.txt`为模板进行代码生成。

### 6.简单的 cmake 代码生成

以`some_script/template/cmake/simple/CMakeLists.txt`为模板进行代码生成。

### 7.模块化组织的 cmake 代码生成

以`some_script/template/cmake/modular_organization`下的cmake结构为模板进行代码生成。该选项需要手动输入生成路径, 输入后则会在对应路径下生成 CMakeLists.txt 文件以及 cmake 目录, 然后在 cmake 目录下生成相应的多个 .cmake 文件。