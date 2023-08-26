import csv

def check_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        lines = sum(1 for _ in reader)
        file.seek(0)
        columns = len(next(reader))
    
    if lines == 26 and columns == 2:
        print("The CSV file has 26 lines and 2 columns.")
    else:
        print("The CSV file does not have 26 lines and 2 columns.")

file_path = "../kb/structured/"
check_csv_file(file_path)
