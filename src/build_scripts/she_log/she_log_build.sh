#!/bin/bash
project="she_db"
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
# Check dir third_party
echo "Check third_party exist?"
if [ -d "./third_party" ];
then
    echo "third_party."
else
    echo "Create third_party."
    mkdir third_party
fi

git clone https://github.com/shecannotsee/she_log.git ./third_party/she_log/

cd third_party
mv she_log she_log-src
# build
mkdir she_log
cd she_log
path=$(pwd)
cmake -DCMAKE_INSTALL_PREFIX=./ ../she_log-src
make -j8
make install
mv she_log/* ./
# Delete all, except for the lib and include directories
shopt -s extglob
rm -rf !(include|lib)
