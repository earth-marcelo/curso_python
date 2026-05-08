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

# reading topography
df_topo = pd.read_csv("topo_erg.txt",
                      sep=r"\s+",
                      header=None,
                      names=["longitude", "latitude", "elevation"])

# Combining 
df = pd.DataFrame({
    "longitude"     : df_267["longitude"],
    "latitude"      : df_267["latitude"],
    "bouguer_267"   : df_267["bouguer_267"],
    "bouguer_290"   : df_290["bouguer_290"],
    "elevation"     : df_topo["elevation"]
})


# Filter: keep only ocean (elevation < -200m)
df_ocean = df[df["elevation"] < -200].reset_index(drop=True)



# Clustering with KMeans - 3 groups
kmeans = KMeans(n_clusters=3, random_state=42)
df_ocean["cluster"] = kmeans.fit_predict(df_ocean[["longitude", "latitude", "bouguer_267", "bouguer_290"]])

print(df_ocean["cluster"].value_counts())

# Cluster map
colors = {0: "blue", 1: "green", 2: "red"}
plt.figure(figsize=(10, 8))
for cluster in [0, 1, 2]:
    mask = df_ocean["cluster"] == cluster
    plt.scatter(df_ocean[mask]["longitude"],
                df_ocean[mask]["latitude"],
                c=colors[cluster],
                s=10,
                label=f"Cluster {cluster}")

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("KMeans clustering - ERG (ocean only)")
plt.legend()
plt.savefig("kmeans-erg.png", dpi=300, bbox_inches="tight")
plt.show()