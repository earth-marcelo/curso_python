import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
import seaborn as sns
from scipy import stats
import numpy as np

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

x = np.array(df_ocean["bouguer_267"])
y = np.array(df_ocean["bouguer_290"])

# Run the regressionspell
results = stats.linregress(x,y)

# Access the results
print(f"Slope: {results.slope}")
print(f"Intercept: {results.intercept}")
print(f"R-squared: {results.rvalue**2}")


# Scatter plot
plt.figure(figsize=(10, 8))

scatter = plt.scatter(df_ocean["bouguer_267"],
                      df_ocean["bouguer_290"],
                      c=df_ocean["elevation"],
                      cmap="RdBu_r",
                      s=10)

slope = results.slope
intercept = results.intercept

line_y = slope * x + intercept

plt.colorbar(scatter, label="Depth (m)")
plt.xlabel("Bouguer Anomaly - 2.67 g/cm3")
plt.ylabel("Bouguer Anomaly - 2.90 g/cm3")
plt.plot(x, line_y, color='black', label='Trendline')
plt.title("Correlation Bouguer anomaly 2.67 vs 2.90 g/cm3")
plt.text(-240, 120, 
         f"y = {slope:.3f}x + {intercept:.3f}\nR² = {results.rvalue**2:.4f}",
         fontsize=10,
         bbox=dict(facecolor='white', edgecolor='black'))
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--')
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--')
plt.savefig("Correlation_bouguer_267_x_290_map.png", dpi=300, bbox_inches="tight")
plt.show()