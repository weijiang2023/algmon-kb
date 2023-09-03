'''
# RENAME files
'''
import os
import os

def rename_files(base_path):
    folder_path = os.path.abspath(base_path)
    file_list = sorted(os.listdir(folder_path))
    for i, file_name in enumerate(file_list):
        if file_name.startswith("Screenshot"):
            print(i, file_name)
            new_name = str(i) + '.png'
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

base_path = "../kb/unstructured/domain.math.grade.6.下/core"
rename_files(base_path)
