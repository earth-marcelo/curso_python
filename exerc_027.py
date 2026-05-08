import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
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

# Boxplot comparing both densities
df_melted = pd.melt(df_ocean,
                    value_vars=["bouguer_267",  "bouguer_290"],
                    var_name="density",
                    value_name="anomaly")

sns.boxplot(x="density", y="anomaly", data=df_melted)
plt.xlabel("Density anomaly (mGal)")
plt.title("Bouguer anomaly - density comparison")
plt.savefig("Bouguer_anomaly_density_comparison.png", dpi=300, bbox_inches="tight")
plt.show()

# Violin plot
sns.violinplot(x="density", y="anomaly", data=df_melted)
plt.xlabel("Density model")
plt.ylabel("Bouguer anomaly (mGal)")
plt.title("Bouguer anomaly distribution - violin plot")
plt.savefig("Bouguer_anomaly_distribution_violin_plot.png", dpi=300, bbox_inches="tight")
plt.show()