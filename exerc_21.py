import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

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
    "longitude"     : df_267["longitude"],
    "latitude"      : df_267["latitude"],
    "bouguer_267"   : df_267["bouguer_267"],
    "bouguer_290"   : df_290["bouguer_290"]
})

# Clustering with KMeans - 3 groups
kmeans = KMeans(n_clusters=3, random_state=42)
df["cluster"] = kmeans.fit_predict(df[["longitude", "latitude", "bouguer_267"]])

print(df["cluster"].value_counts())
print()
print(df.groupby("cluster")["bouguer_267"].describe())

# Cluster map
colors = {0: "blue", 1: "green", 2: "red"}
plt.figure(figsize=(10, 8))
for cluster in [0, 1, 2]:
    mask = df["cluster"] == cluster
    plt.scatter(df[mask]["longitude"],
                df[mask]["latitude"],
                c=colors[cluster],
                s=10,
                label=f"Cluster     {cluster}")

plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("KMeans clustering - ERG area")
plt.legend()
plt.show()