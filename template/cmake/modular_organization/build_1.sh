#!/bin/bash
project="modular_organization"
project_length=${#project}
# Get pwd string
path=$(pwd)
# Get last project_length chars
suffix="${path: -$project_length}"
if [ "$suffix" = "$project" ]; then
    echo "ok"
else
    echo "Path error.Please ensure that the last few strings after using pwd are "$project
    exit 1  # stop
fi
# check dir build
echo "Check libraries exist?"
if [ -d "./build" ];
then
    rm -rf ./build
    echo "build."
else
    echo "Create build."
fi

mkdir build
cd build


cmake -DCMAKE_INSTALL_PREFIX=./ .. || { echo "CMake execution failed"; exit 1; }

make -j9 || { echo "Make execution failed"; exit 1; }
make install || { echo "Make install failed"; exit 1; }

echo "static-lib, test, debug"
