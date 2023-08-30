import chardet
import pandas as pd
import os

'''
# step 1: detect
def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

# Example usage
file_path = '../kb/structured/domain.math.grade.5.上/练习1.qa.csv'
if os.path.exists(file_path):
    print("The file path is valid.")
else:
    print("The file path is not valid.")
encoding = detect_csv_encoding(file_path)
print(f"The encoding of the CSV file is: {encoding}")
'''

# step 2: convert
def convert_csv_encoding(input_file, output_file, input_encoding, output_encoding):
    df = pd.read_csv(input_file, encoding=input_encoding)
    df.to_csv(output_file, encoding=output_encoding, index=False)

# Example usage
input_file = '../kb/structured/domain.math.grade.5.上/OLD.练习3.qa.csv'
output_file = '../kb/structured/domain.math.grade.5.上/练习3.qa.csv'
input_encoding = 'GB2312'
output_encoding = 'UTF-8'

convert_csv_encoding(input_file, output_file, input_encoding, output_encoding)
