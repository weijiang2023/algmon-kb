"""
Convert the given csv files to specific encoding
"""
import pandas as pd

def convert_csv_encoding(input_file, output_file, input_encoding, output_encoding):
    df = pd.read_csv(input_file, encoding=input_encoding)
    df.to_csv(output_file, encoding=output_encoding, index=False)

# Example usage
input_file = '../kb/structured/domain.math.grade.5.上/OLD/练习19.qa.csv'
output_file = '../kb/structured/domain.math.grade.5.上/练习19.qa.csv'
input_encoding = 'GB2312'
output_encoding = 'UTF-8'

convert_csv_encoding(input_file, output_file, input_encoding, output_encoding)
