"""
Detect the encoding of the csv files
"""
import chardet

def check_csv_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        #print(f"The encoding of the CSV file is: {encoding}")
        if encoding != "UTF-8-SIG":
            print(file)

base_path = "../kb/structured/domain.math.grade.5.上/"
cnt = 0
files = []
for i in range(0, 16):
    relative_file_name = str(i).zfill(2) + ".qa.csv"
    complete_file_name = base_path + relative_file_name
    files.append(complete_file_name)

for file in files:
    #print(file)
    check_csv_encoding(file)