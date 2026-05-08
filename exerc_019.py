import pandas as pd

# Reading the files
df_267 = pd.read_csv("bouguer_erg_267.txt",
                     sep=r"\s+",
                     header=None,
                     names=["longitude", "latitude", "bouguer_267"])

df_290 = pd.read_csv("bouguer_erg_290.txt",
                     sep=r"\s+",
                     header=None,
                     names=["longitude", "latitude", "bouguer_290"])

# Combining
df = pd.DataFrame({
    "longitude": df_267["longitude"],
    "latitude" : df_267["latitude"],
    "bouguer_267" : df_267["bouguer_267"],
    "bouguer_290" :df_290["bouguer_290"]
})

# Filtering positive anomalies
df_positive = df[df["bouguer_267"]  > 0]

# Filtering negative anomalies
df_negative = df[df["bouguer_267"]  < 0]

print("Total points:", len(df))
print("Positive anomalies:", len(df_positive))
print("Negative anomalies:", len(df_negative))

#Filtering ERG area
df_erg = df[(df["longitude"] >= -33) & (df["longitude"] <= -31) & (df["latitude"] >= -30)  & (df["latitude"]  <= -28)]   

print("ERG points:", len(df_erg))
print()
print(df_erg["bouguer_267"].describe())