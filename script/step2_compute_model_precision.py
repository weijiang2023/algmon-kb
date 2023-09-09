from natsort import natsorted
import pandas as pd
import os

def compute_model_precision(csv_file):
    df = pd.read_csv(csv_file)
    pass_rate = df[df['机器回答通过与否'] == '通过'].shape[0] / df.shape[0]
    avg_satisfaction = df['满意度'].mean()
    
    #pass_rate = df['机器回答通过与否'].mean()
    avg_satisfaction = df['满意度'].mean()
    return pass_rate, avg_satisfaction

def return_precision_para(csv_file):
    df = pd.read_csv(csv_file)
    return df['满意度'].sum(), df[df['机器回答通过与否'] == '通过'].shape[0], df.shape[0]

def return_todo_para(csv_file):
    df = pd.read_csv(csv_file)
    return df[df['机器回答通过与否'] == '未验证'].shape[0]

base_paths = []
base_path_0 = "../kb/structured/domain.教培/domain.math.grade.5.up/"
base_path_1 = "../kb/structured/domain.教培/domain.math.grade.5.down/"
base_paths.append(base_path_0)
base_paths.append(base_path_1)

files = []
for base_path in base_paths:
    # List all files in the directory
    file_list = os.listdir(base_path)

    # Sort the file list
    file_list = natsorted(file_list)
    for file in file_list:
        #print(file)
        if file.startswith("ex"):
            files.append(base_path + file)

score = 0.0
num_pass = 0
num_total = 0
num_todo_files = 0

for file in files:
    #print(file)
    (x, y, z) = return_precision_para(file)
    if x == 6 and y == 1 and z == 1:
        num_todo_files += 1
    else:
        print(file, x, y, z)
        score += x
        num_pass += y
        num_total += z

print("Model Precision")
print("total pass:", num_pass)
print("total run:", num_total)
print("sum score:", score)
print("avg score:", score / num_pass)
print("pass rate:", num_pass / num_total)
print("num todo files:", num_todo_files)