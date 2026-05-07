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


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Map 2.67
sc1 = ax1.scatter(df_ocean["longitude"],
                  df_ocean["latitude"],
                  c=df_ocean["bouguer_267"],
                  cmap="RdBu_r",
                  s=10)
plt.colorbar(sc1, ax=ax1, label="Bouguer anomaly (mGal)")
ax1.set_xlabel("longitude")
ax1.set_ylabel("latitude")
ax1.set_title("Density 2.67 gm/cm3")


# Map 2.90
sc2 = ax2.scatter(df_ocean["longitude"],
                  df_ocean["latitude"],
                  c=df_ocean["bouguer_290"],
                  cmap="RdBu_r",
                  s=10)
plt.colorbar(sc2, ax=ax2, label="Bouguer anomaly (mGal)")
ax2.set_xlabel("longitude")
ax2.set_ylabel("latitude") 
ax2.set_title("Density 2.90 gm/cm3")

plt.suptitle("Bouguer anomaly comparison - ERG area")
plt.tight_layout()
plt.savefig("bouguer_anomaly_comparison.png", dpi=300, bbox_inches="tight")
plt.show()


fig, (axes) = plt.subplots(1, 2, figsize=(16, 8))
#histogram 2.67
sns.histplot(df_ocean["bouguer_267"], bins=30, color="steelblue",ax=axes[0])
axes[0].set_title("Bouguer anomaly distribution - density 2.67 g/cm3")
axes[0].set_xlabel("Bouguer anomaly (mGal)")

#histogram 2.90
sns.histplot(df_ocean["bouguer_290"], bins=30, color="steelblue", ax=axes[1])
axes[1].set_title("Bouguer anomaly distribution - density 2.90 g/cm3")
axes[1].set_xlabel("Bouguer anomaly (mGal)")

plt.savefig("bouguer_anomaly_histogram_comparison.png", dpi=300, bbox_inches="tight")
plt.tight_layout()
plt.show()

