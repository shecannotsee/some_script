#!/bin/bash

# tips
read -p "The library name and version are (like xxx-0.0.0): " library_name

# create directory
directory="./libraries/$library_name"
mkdir -p "$directory"

# create describe.md
describe_file="$directory/describe.md"
touch "$describe_file"

# create xx_build.sh
build_file="$directory/${library_name}_build.sh"
touch "$build_file"

echo "success!"
