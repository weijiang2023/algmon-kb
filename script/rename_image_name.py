'''
# RENAME files
'''
from natsort import natsorted
import os

def rename_files(base_path):
    folder_path = os.path.abspath(base_path)
    file_list = natsorted(os.listdir(folder_path), key=str.lower)
    for i, file_name in enumerate(file_list):
        if file_name.endswith(".png"):
            new_name = str(i+1) + '.png'
            print(i, file_name, new_name)
            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))

base_path = "../kb/unstructured/domain.教培/math/grade.6"
rename_files(base_path)
