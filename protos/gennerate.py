import os

# Define the directory containing the PB files
pb_dir = "./pb_dir"
# Define the name of the new PB file
new_pb_file = "merge/particle.proto"

# Clear the content of the new file
with open(new_pb_file, 'w') as f:
    f.write('')

# Copy the content of all files to the new file and remove the lines with "package" and "import"
for root, dirs, files in os.walk(pb_dir):
    for pb_file_name in files:
        if pb_file_name.endswith('.proto'):
            pb_file = os.path.join(root, pb_file_name)
            # Exclude "syntax", "package" and "import" lines
            with open(pb_file, 'r') as f:
                lines = f.readlines()
            lines = [line for line in lines if
                     not line.startswith('package') and not line.startswith('import') and not line.startswith('syntax')]
            with open(new_pb_file, 'a') as f:
                f.writelines(lines)

# Remove extra blank lines
with open(new_pb_file, 'r') as f:
    lines = f.readlines()
with open(new_pb_file, 'w') as f:
    for line in lines:
        if line.strip():
            f.write(line)

# Add "syntax" , "package" and "new line" lines to the beginning of the file
with open(new_pb_file, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
    f.write("syntax = \"proto3\";\n")
    f.write("package com.yunlong.particle.proto;\n")
    f.write("\n")
    f.write(content)
