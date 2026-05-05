import pandas as pd

# Reading the CSV file
df = pd.read_csv("bouguer.csv")

# Visualizing the data

print(df)
print(df.head())        # first five lines
print(df.tail())        # last five lines
print(df.info())        # column information
print(df.describe())    # automatic statistics!