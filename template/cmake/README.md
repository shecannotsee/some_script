

- 该模板下的magic_string如下

  md5("sheer")=**afa05a6348902c252ae10d48879826b3**

- 构建类型：通常的cmake项目会通过指定`CMAKE_BUILD_TYPE=Release`来处理构建类型，例如`cmake -DCMAKE_BUILD_TYPE=Release ..`

- 安装路径：通常使用`CMAKE_INSTALL_PREFIX`，例如`cmake -DCMAKE_INSTALL_PREFIX=./ ..`

- 构建测试：通常使用`BUILD_TESTS`，例如`cmake -DBUILD_TESTS=OFF ..`

- 对于一些库目录的指定，一般通过`XXX_ROOT_DIR`，例如指定boost库目录`cmake -DBOOST_ROOT_DIR=./boost ..`

- 常用的cmake命令`cmake -DCMAKE_INSTALL_PREFIX=./ -DCMAKE_BUILD_TYPE=Release ..`

