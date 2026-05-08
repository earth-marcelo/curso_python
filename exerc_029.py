import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import seaborn as sns

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

df_ocean["difference"] = df_ocean["bouguer_290"] - df_ocean["bouguer_267"]


# Scatter plot
plt.figure(figsize=(10, 8))

scatter = plt.scatter(df_ocean["longitude"],
                      df_ocean["latitude"],
                      c=df_ocean["difference"],
                      cmap="RdBu_r",
                      s=10)

plt.colorbar(scatter, label="Anomaly (mGal)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Bouguer anomaly difference (2.90 - 2.67 g/cm³)")
plt.savefig("Bouguer_anomaly_difference.png", dpi=300, bbox_inches="tight")
plt.show()


# Seaborn histogram
sns.histplot(df_ocean["difference"], bins=30, color="steelblue")
plt.xlabel("Anomaly (mGal)")
plt.ylabel("Count")
plt.title("Bouguer anomaly difference (2.90 - 2.67 g/cm³)")
plt.show()