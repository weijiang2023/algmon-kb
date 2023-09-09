"""
Convert the given csv files to specific encoding
"""
import chardet
import pandas as pd
from natsort import natsorted
import os

def convert_csv_encoding(input_file, output_file, input_encoding, output_encoding):
    df = pd.read_csv(input_file, encoding=input_encoding)
    df.to_csv(output_file, encoding=output_encoding, index=False)

def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

# Example usage
files = []
base_path = "../kb/structured/domain.教培/domain.math.grade.5.down/"

# List all files in the directory
file_list = os.listdir(base_path)

# Sort the file list
file_list = natsorted(file_list)

# Append the base path to each file name
for idx,input_file in enumerate(file_list):
    if input_file.startswith("ex"):
        encoding = detect_csv_encoding(base_path + input_file)
        print(input_file, encoding)
        if encoding == "GB2312":
            print("Needs Conversion")
            output_file = base_path + '/NEW/' + input_file
            input_encoding = 'GB2312'
            output_encoding = 'UTF-8'
            convert_csv_encoding(base_path + input_file, output_file, input_encoding, output_encoding)
