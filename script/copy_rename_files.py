import shutil
import os

source_file = "../kb/structured/domian.math.grade.5.上/练习二.qa.csv"
destination_folder = "../kb/structured/domian.math.grade.5.上/"

for i in range(3, 25):
    destination_file = f"练习{i}.qa.csv"
    shutil.copy(source_file, os.path.join(destination_folder, destination_file))
