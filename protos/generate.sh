# Define the directory containing the PB files
pb_dir="./pb_dir"
# Define the name of the new PB file
new_pb_file="merge/particle.proto"

# Define the directory of Python file
new_py_dir="../particle/protos"

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
echo "package com.yunlong.particle.proto;" | cat - "${new_pb_file}" >temp && mv temp "${new_pb_file}"
echo "syntax = 'proto3';" | cat - "${new_pb_file}" >temp && mv temp "${new_pb_file}"


protoc --python_out=${new_py_dir} ${new_pb_file}
