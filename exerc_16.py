import pandas as pd

# Reading the file without header
df = pd.read_csv("bouguer_erg_267.txt",
                 sep=r"\s+",
                 header=None,
                 names=["longitude", "latitude", "bouguer"])

# visualizing
print(df.head())
print()
print(df.info())
print()
print(df.describe())
