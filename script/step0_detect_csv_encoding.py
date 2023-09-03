"""
Detect the encoding of the given csv files
"""
import chardet
import pandas as pd

def detect_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    return encoding

# Example usage
files = []
file_1 = "../kb/structured/domain.math.grade.5.上/练习1.qa.csv"
file_2 = "../kb/structured/domain.math.grade.5.上/练习2.qa.csv"
file_3 = "../kb/structured/domain.math.grade.5.上/练习3.qa.csv"
file_4 = "../kb/structured/domain.math.grade.5.上/练习4.qa.csv"
file_5 = "../kb/structured/domain.math.grade.5.上/练习5.qa.csv"
file_6 = "../kb/structured/domain.math.grade.5.上/练习6.qa.csv"
file_7 = "../kb/structured/domain.math.grade.5.上/练习7.qa.csv"
file_8 = "../kb/structured/domain.math.grade.5.上/练习8.qa.csv"
file_9 = "../kb/structured/domain.math.grade.5.上/练习9.qa.csv"
file_10 = "../kb/structured/domain.math.grade.5.上/练习10.qa.csv"
file_11 = "../kb/structured/domain.math.grade.5.上/练习11.qa.csv"
file_12 = "../kb/structured/domain.math.grade.5.上/练习12.qa.csv"
file_13 = "../kb/structured/domain.math.grade.5.上/练习13.qa.csv"
file_14 = "../kb/structured/domain.math.grade.5.上/练习14.qa.csv"
file_15 = "../kb/structured/domain.math.grade.5.上/练习15.qa.csv"
file_16 = "../kb/structured/domain.math.grade.5.上/练习16.qa.csv"
file_17 = "../kb/structured/domain.math.grade.5.上/练习17.qa.csv"
file_18 = "../kb/structured/domain.math.grade.5.上/练习18.qa.csv"
file_19 = "../kb/structured/domain.math.grade.5.上/练习19.qa.csv"
file_20 = "../kb/structured/domain.math.grade.5.上/练习20.qa.csv"
file_21 = "../kb/structured/domain.math.grade.5.上/练习21.qa.csv"
file_22 = "../kb/structured/domain.math.grade.5.上/练习22.qa.csv"
file_23 = "../kb/structured/domain.math.grade.5.上/练习23.qa.csv"
file_24 = "../kb/structured/domain.math.grade.5.上/练习24.qa.csv"
file_25 = "../kb/structured/domain.math.grade.5.上/练习25.qa.csv"
'''
files.append(file_1)
files.append(file_2)
files.append(file_3)
files.append(file_4)
files.append(file_5)
files.append(file_6)
files.append(file_9)
files.append(file_10)
files.append(file_12)
files.append(file_13)
files.append(file_14)
files.append(file_15)
files.append(file_16)
files.append(file_17)
files.append(file_18)
files.append(file_19)
files.append(file_20)
files.append(file_21)
files.append(file_24)
files.append(file_25)
'''
files.append(file_7)
files.append(file_8)
files.append(file_11)
files.append(file_22)
files.append(file_23)

for file in files:
    encoding = detect_csv_encoding(file)
    print(file)
    print(f"The encoding of the CSV file is: {encoding}")
    print("\n")