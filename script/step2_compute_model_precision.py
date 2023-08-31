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

def return_todo_para(csv_file):
    df = pd.read_csv(csv_file)
    return df[df['机器回答通过与否'] == '未验证'].shape[0]

files = []
todo_files = []
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

todo_files.append(file_7)
todo_files.append(file_8)
todo_files.append(file_11)
todo_files.append(file_22)
todo_files.append(file_23)

todo_num = 0
for file in todo_files:
    z = return_todo_para(file)
    print(file, z)
    todo_num += z

print("***** *****")

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
print("未验证:", todo_num)