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