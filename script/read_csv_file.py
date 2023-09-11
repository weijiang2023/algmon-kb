import pandas as pd

file_path = "../kb/structured/domain.教培/domain.math.grade.5.down/TODO/ex19.qa.csv"
# Read the csv file
df = pd.read_csv(file_path)

# Sort the file by name
df = df.sort_values(by='name')

# Print the sorted dataframe
print(df)
