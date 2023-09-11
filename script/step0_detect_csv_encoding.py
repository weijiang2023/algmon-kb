"""
Detect the encoding of the given csv files
"""
import chardet
import pandas as pd
from natsort import natsorted
import os

def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

# Example usage
files = []
base_path = "../kb/structured/domain.教培/domain.math.grade.5.down/TODO/"

# List all files in the directory
file_list = os.listdir(base_path)

# Sort the file list
file_list = natsorted(file_list)

# Append the base path to each file name
for idx,file in enumerate(file_list):
    if file.startswith("ex"):
        encoding = detect_csv_encoding(base_path + file)
        print(file, encoding)