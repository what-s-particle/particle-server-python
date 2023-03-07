#!/bin/bash

# Set the directory path
dir_path="./protos"

# Delete all files and subdirectories in the directory
rm -rf $dir_path/*

# Create a new, empty directory if it does not exist
if [ ! -d "$dir_path" ]; then
  mkdir $dir_path
fi

# Set the proto repository name and target directory
repo_name="particle-protocol"
target_dir="protos"

# Clone the repository
git clone https://github.com/what-s-particle/$repo_name.git

# Remove all files and directories except for the target directory
cd $repo_name
find . ! -path "./$target_dir*" -delete

# Move the target directory to the current directory
cd ..

mv $repo_name/$target_dir .

# Remove the cloned repository
rm -rf $repo_name

# Define the directory containing the PB files
pb_dir="./protos"
# Define the name of the new PB file
new_pb_dir="./generate"
new_pb_file="./generate/particle.proto"

# Define the directory of Python file
gen_py_dir="./generate/python"

# Define the directory of Python file
new_py_dir="../protos"

rm -rf $new_pb_dir/*
if [ ! -d "$new_pb_dir" ]; then
  mkdir $new_pb_dir
fi

# Delete all files and subdirectories in the build directory
rm -rf $gen_py_dir/*
if [ ! -d "$gen_py_dir" ]; then
  mkdir $gen_py_dir
fi

rm -rf $new_py_dir/*
if [ ! -d "$new_py_dir" ]; then
  mkdir $new_py_dir
fi

# Clear the content of the new file
echo "" >"${new_pb_file}"

# Recursively search for PB files in the specified directory
for pb_file in $(find "${pb_dir}" -name "*.proto"); do
  # Exclude "syntax", "package" and "import" lines
  grep -v '^syntax' "${pb_file}" | grep -v '^package' | grep -v '^import' >>"${new_pb_file}"
done

# Remove extra blank lines
sed -i '/^$/d' "${new_pb_file}"

# Add a new line after each '}'
sed -i '/}/{G;}' "${new_pb_file}"

# Add "syntax" , "import" and "new line" lines to the beginning of the file
echo "" | cat - "${new_pb_file}" >temp && mv temp "${new_pb_file}"
#echo "package com.yunlong.particle.proto;" | cat - "${new_pb_file}" >temp && mv temp "${new_pb_file}"
echo "syntax = 'proto3';" | cat - "${new_pb_file}" >temp && mv temp "${new_pb_file}"

# generate `.pyi` https://github.com/protocolbuffers/protobuf/issues/10988
protoc --python_out=${gen_py_dir} --pyi_out=${gen_py_dir} ${new_pb_file}

# Rename "xxx_pb2.py" to "xxx.py"
for file  in $(find "${gen_py_dir}" -name "*.py"); do
    new_name=${file/_pb2/}
    mv "${file}" "${new_name}"
done

for file  in $(find "${gen_py_dir}" -name "*.pyi"); do
    new_name=${file/_pb2/}
    mv "${file}" "${new_name}"
done

# Move each subdirectory to the parent directory
mv "${gen_py_dir}/generate" "${new_py_dir}"

for subdir in $new_py_dir/*; do
  if [ -d "$subdir" ]; then
    mv "$subdir"/* "$new_py_dir"
    rmdir "$subdir"
  fi
done

rm -rf $new_pb_file
rm -rf "${pb_dir}"
rm -rf "${new_pb_dir}"
