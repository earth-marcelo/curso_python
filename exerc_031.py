import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import cmocean


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

# Scatter plot
plt.figure(figsize=(10, 8))

scatter = plt.scatter(df_ocean["longitude"],
                      df_ocean["latitude"],
                      c=df_ocean["elevation"],
                      cmap=cmocean.cm.deep_r,
                      s=10)

plt.colorbar(scatter, label="meters (m)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Bathymetry - ERG area")
plt.savefig("Bathymetry_ERG area.png", dpi=300, bbox_inches="tight")
plt.show()