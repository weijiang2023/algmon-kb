import shutil
import os

source_file = "../kb/structured/domain.math.grade.5.下/练习1.qa.csv"
destination_folder = "../kb/structured/domain.math.grade.5.下/"

for i in range(2, 28):
    destination_file = f"练习{i}.qa.csv"
    shutil.copy(source_file, os.path.join(destination_folder, destination_file))
