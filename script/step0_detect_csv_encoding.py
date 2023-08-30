"""
Detect the encoding of the given csv files
"""
import chardet
import chardet
import pandas as pd
import os

def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

# Example usage
files = []
file_0 = '../kb/structured/domain.math.grade.5.上/练习17.qa.csv'
file_1 = '../kb/structured/domain.math.grade.5.上/练习18.qa.csv'
file_2 = '../kb/structured/domain.math.grade.5.上/练习19.qa.csv'
file_3 = '../kb/structured/domain.math.grade.5.上/练习20.qa.csv'
files.append(file_0)
files.append(file_1)
files.append(file_2)
files.append(file_3)
for file in files:
    encoding = detect_csv_encoding(file)
    print(f"The encoding of the CSV file is: {encoding}")