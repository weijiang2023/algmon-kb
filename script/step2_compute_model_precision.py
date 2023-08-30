import pandas as pd

def compute_model_precision(csv_file):
    df = pd.read_csv(csv_file)
    pass_rate = df[df['机器回答通过与否'] == '通过'].shape[0] / df.shape[0]
    avg_satisfaction = df['满意度'].mean()
    
    #pass_rate = df['机器回答通过与否'].mean()
    avg_satisfaction = df['满意度'].mean()
    return pass_rate, avg_satisfaction

#pass_rate, avg_satisfaction = compute_model_precision(csv_file_1)
#print(pass_rate, avg_satisfaction)

def return_precision_para(csv_file):
    df = pd.read_csv(csv_file)
    return df['满意度'].sum(), df[df['机器回答通过与否'] == '通过'].shape[0], df.shape[0]

files = []
file_1 = "../kb/structured/domain.math.grade.5.上/练习1.qa.csv"
file_2 = "../kb/structured/domain.math.grade.5.上/练习2.qa.csv"
file_3 = "../kb/structured/domain.math.grade.5.上/练习3.qa.csv"
file_4 = "../kb/structured/domain.math.grade.5.上/练习4.qa.csv"
#
file_17 = "../kb/structured/domain.math.grade.5.上/练习17.qa.csv"
file_18 = "../kb/structured/domain.math.grade.5.上/练习18.qa.csv"
file_19 = "../kb/structured/domain.math.grade.5.上/练习19.qa.csv"
file_20 = "../kb/structured/domain.math.grade.5.上/练习20.qa.csv"

files.append(file_1)
files.append(file_2)
files.append(file_3)
files.append(file_4)
files.append(file_17)
files.append(file_18)
files.append(file_19)
files.append(file_20)

score = 0.0
num_pass = 0
num_total = 0

for file in files:
    (x, y, z) = return_precision_para(file)
    print(file, z)
    score += x
    num_pass += y
    num_total += z

print("Model Precision")
print("total pass:", num_pass)
print("total run:", num_total)
print("sum score:", score)
print("avg score:", score / num_pass)
print("pass rate:", num_pass / num_total)