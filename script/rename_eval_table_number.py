'''
# RENAME files
'''
from natsort import natsorted
import os

base_path = "../kb/structured/domain.教培/domain.math.grade.5.down/"

# List all files in the directory
file_list = os.listdir(base_path)

# Sort the file list
file_list = natsorted(file_list)

for idx,file in enumerate(file_list):
    print(file)
    if file.startswith("练习"):
        new_name = "ex" + file[2:]
        print(idx, file, new_name)
        os.rename(os.path.join(base_path, file), os.path.join(base_path, new_name))
    else:
        print("Mark1")