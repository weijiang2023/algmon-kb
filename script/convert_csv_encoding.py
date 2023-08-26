import pandas as pd

files = [
    #"../kb/structured/00.qa.csv",
    #"../kb/structured/01.qa.csv",
    ##"../kb/structured/02.qa.csv",
    #"../kb/structured/03.qa.csv",
    ##"../kb/structured/04.qa.csv",
    #"../kb/structured/05.qa.csv",
    #"../kb/structured/07.qa.csv"
]

for file in files:
    # Read the file
    df = pd.read_csv(file)
    # Convert the file to UTF-8-SIG encoding
    df.to_csv(file, encoding='utf-8-sig', index=False)