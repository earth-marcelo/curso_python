import pandas as pd

# Reading both files
df_267 = pd.read_csv("bouguer_erg_267.txt",
                     sep=r"\s+",
                     header=None,
                     names=["longitude", "latitude", "bouguer_267"])

df_290 = pd.read_csv("bouguer_erg_290.txt",
                     sep=r"\s+",
                     header=None,
                     names=["longitude", "latitude", "bouguer_290"])

# Combining into a single DataFrame
df = pd.DataFrame({
    "longitude"     : df_267["longitude"],
    "latitude"      : df_267["latitude"],
    "bouguer_267"   : df_267["bouguer_267"],
    "bouguer_290"   : df_290["bouguer_290"]  
})

df["difference"] = df["bouguer_290"] -df["bouguer_267"]

print(df.head())
print()
#print(df.describe())
print (df["difference"].describe())