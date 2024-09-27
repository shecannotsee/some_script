# modular_organization

## 一、总体设想

#### 代码和产出

对于一个 c++ 项目(这里将项目名取为 cpp_project_template ), 必须的 target 是源代码和测试代码组成的两组产出。

- src 目录以及其对应的产出
- test 目录以及其对应的产出
- 其他目录以及对应的产出



#### 项目的编译设置

- 编译目标: Debug 还是 Release, 使用`CMAKE_BUILD_TYPE`
- 构建测试模块, 使用`BUILD_TESTS`
- 安装目录, 使用`CMAKE_INSTALL_PREFIX`
- 第三方库的传递路径, 使用`XXX_ROOT_DIR`



#### c++项目设置

- 语言标准: c++11、14、17、20(`-fcoroutines`) 等
- 编译命令: `-g`、`-O2`等



## 二、实际项目结构与细节

### 1.目录结构

```bash
$ tree -L 2
.
├── build_1.sh
├── build_2.sh
├── build_3.sh
├── build_gtest.sh
├── cmake
│   ├── build.cmake
│   ├── import_third_party.cmake
│   ├── install.cmake
│   ├── target_src.cmake
│   └── target_test.cmake
├── CMakeLists.txt
├── googletest-1.12.0
│   ├── include
│   └── lib
├── README_CN.md
├── src
│   ├── cal.cpp
│   └── cal.h
└── test
    ├── cal.cpp
    └── main.cpp

6 directories, 15 files
$
```

这里仅描述 cmake 相关的文件与作用

### 2.CMakeLists.txt

该文件主要处理构建的的全局信息和前置变量, 以及 include 子文件

1. 全局信息: 项目名、项目版本、项目语言
2. 全局选项: 是否构建 release、是否构建测试、是否构建动态库
3. 一些需要提前声明的固定信息: src 目录、src 链接变量、test 名、test 链接变量
4. 按照顺序包含的 cmake 子文件

自定义以及添加的内容: 若要添加额外的 target , 需要参考 test 的模块的处理方式, 额外声明 target 名和链接变量, 然后添加相应的 cmake 子文件, 若有需要, 则还需要在 cmake/import_third_party.cmake 中添加链接, 在 cmake/install.cmake 中添加相应的安装方式。



### 3.cmake 目录

#### (1)build.cmake

该文件主要处理编译命令以及 c++ 的一些标准

1. 语言标准: c++ 标准设置
2. 编译指令: 构件类型、优化等级、以及其他的一些编译指令

自定义以及添加的内容: 若要添加额外的编译指令, 则可以参考该文件的模板进行指令的添加。



#### (2)import_third_party.cmake

该文件主要处理第三方库的引入问题。

自定义以及添加的内容: 可以参考对 test 模块引入 gtest 的方式, 为其他 target 引入其他第三方库。



#### (3)target_src.cmake

该文件主要处理 src 中的 target 生成, 默认 src 的代码生成一个静态库, 根据全局选项还可以额外生成一个动态库。并且还有一个 header list 用来声明所有的 .h 和 .hpp 文件, 便于安装模块的安装。

自定义以及添加的内容: 该文件通常无需变动或者更改。



#### (4)target_test.cmake

该文件主要处理  test 中的 target 生成, 也可以作为其他 target 构建的样例。

自定义以及添加的内容: 该文件通常无需变动或者更改。



#### (5)install.cmake

该文件主要处理构建项目后的安装问题。首先是默认安装 src 的所有内容, 然后根据选项选择性的安装动态库以及测试模块。

自定义以及添加的内容: 根据额外添加的 target 可以参考 target test 的代码样例进行安装。



#### (6)自定义文件

对于额外添加的名为 sample 的 target , sample需要先在 CMakeLists.txt 中参考 target-test 添加全局信息, 然后在 include 中添加名为 target_sample.cmake 的 cmake 文件。然后在 cmake/import_third_party.cmake 中对 sample 添加相应的依赖。然后在 target_sample.cmake 中处理构建目录以及构建目标。最后在 cmake/install.cmake 中添加相应的安装方式。



