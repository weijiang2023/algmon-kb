import pandas as pd
import os

base_path = "../kb/structured/domain.math.grade.5.上/"

# List all the files under this folder
file_list = os.listdir(base_path)
for file in file_list:
    if file.startswith("练习"):
        print(base_path + file)
        # Read the CSV file
        df = pd.read_csv(base_path + file)
        # Check if 'number' column exists
        if 'number' not in df.columns:
            # Add 'number' column and fill with increasing values
            df['number'] = range(1, len(df) + 1)
            # Save the modified DataFrame back to CSV
            df.to_csv(base_path + 'NEW/' + file, index=False)
