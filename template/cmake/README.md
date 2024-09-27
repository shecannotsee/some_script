

- The `magic_string` under this template is as follows:

  md5("sheer")=**afa05a6348902c252ae10d48879826b3**

- Build Type: Typically, CMake projects handle the build type by specifying `CMAKE_BUILD_TYPE=Release`, for example, `cmake -DCMAKE_BUILD_TYPE=Release ..`

- Installation Path: Usually specified with `CMAKE_INSTALL_PREFIX`, for example, `cmake -DCMAKE_INSTALL_PREFIX=./ ..`

- Build Tests: Typically controlled using `BUILD_TESTS`, for example, `cmake -DBUILD_TESTS=OFF ..`

- For specifying the directory of some libraries, it is generally done through `XXX_ROOT_DIR`, for example, to specify the Boost library directory: `cmake -DBOOST_ROOT_DIR=./boost ..`

- Common CMake command: `cmake -DCMAKE_INSTALL_PREFIX=./ -DCMAKE_BUILD_TYPE=Release ..`

