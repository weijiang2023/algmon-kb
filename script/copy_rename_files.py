"""
COPY and RENAME files for repetition
"""
import shutil
import os

source_file = "../kb/structured/domain.教培/domain.math.grade.6/ex.1.qa.csv"
destination_folder = "../kb/structured/domain.教培/domain.math.grade.6/"

for i in range(2, 24):
    destination_file = f"ex.{i}.qa.csv"
    print(destination_file)
    shutil.copy(source_file, os.path.join(destination_folder, destination_file))
