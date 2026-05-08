import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the file
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

# Seaborn histogram
sns.histplot(df["bouguer_267"], bins=30, color="steelblue")
plt.xlabel("Bouguer anomaly (mGal)")
plt.ylabel("Count")
plt.title("Bouguer anomaly distribution - density 2.67")
plt.show()

# Boxplot comparing both densities
df_melted = pd.melt(df,
                    value_vars=["bouguer_267",  "bouguer_290"],
                    var_name="density",
                    value_name="anomaly")

sns.boxplot(x="density", y="anomaly", data=df_melted)
plt.xlabel("Density anomaly (mGal)")
plt.title("Bouguer anomaly - density comparison")
plt.show()

# Violinplot
sns.violinplot(x="density", y="anomaly", data=df_melted)
plt.xlabel("Density model")
plt.ylabel("Bouguer anomaly (mGal)")
plt.title("Bouguer anomaly distribution - violin plot")
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(),
            annot=True,
            cmap="RdBu_r",
            fmt=".2f")
plt.title("Correlation matrix")
plt.show()