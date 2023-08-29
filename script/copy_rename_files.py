import shutil
import os

source_file = "../kb/structured/domain.math.grade.5.上/old/练习5.qa.csv"
destination_folder = "../kb/structured/domain.math.grade.5.上/old/"

for i in range(6, 25):
    destination_file = f"练习{i}.qa.csv"
    shutil.copy(source_file, os.path.join(destination_folder, destination_file))
