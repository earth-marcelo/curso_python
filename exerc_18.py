import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

# Reading the files
df_267 = pd.read_csv("bouguer_erg_267.txt",
                     sep=r"\s+",
                     header=None,
                     names=["longitude", "latitude", "bouguer_267"])

df_290 = pd.read_csv("bouguer_erg_290.txt",
                     sep=r"\s+",
                     names=["longitude", "latitude", "bouguer_290"])

# Combining
df = pd.DataFrame({
    "longitude"     :   df_267["longitude"],
    "latitude"      :   df_267["latitude"],
    "bouguer_267"   :   df_267["bouguer_267"],
    "bouguer_290"   :   df_290["bouguer_290"],
})

# Simple histogram
plt.hist(df["bouguer_267"], bins=30, color="blue", alpha=0.7)
plt.xlabel("Bouguer anomaly (mGal)")
plt.ylabel("Count")
plt.title("Bouguer anomaly distribution - density 2.67")
plt.show()

# Scatter plot
plt.figure(figsize=(10, 8))

scatter = plt.scatter(df["longitude"],
                      df["latitude"],
                      c=df["bouguer_267"],
                      cmap="RdBu_r",
                      s=10)

plt.colorbar(scatter, label="Bouguer anomaly (mGal)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Bouguer anomaly - density 2.67")
plt.savefig("bouguer_267_map.png", dpi=300, bbox_inches="tight")
plt.show()

print("longitude:", df["longitude"].min(), "to", df["longitude"].max())
print("latitude:",  df["latitude"].min(),  "to", df["latitude"].max())


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Map 2.67
sc1 = ax1.scatter(df["longitude"],
                  df["latitude"],
                  c=df["bouguer_267"],
                  cmap="RdBu_r",
                  s=10)
plt.colorbar(sc1, ax=ax1, label="Bouguer anomaly (mGal)")
ax1.set_xlabel("longitude")
ax1.set_ylabel("latitude")
ax1.set_title("Density 2.67 gm/cm3")


# Map 2.90
sc2 = ax2.scatter(df["longitude"],
                  df["latitude"],
                  c=df["bouguer_290"],
                  cmap="RdBu_r",
                  s=10)
plt.colorbar(sc2, ax=ax2, label="Bouguer anomaly (mGal)")
ax2.set_xlabel("longitude")
ax2.set_ylabel("latitude")
ax2.set_title("Density 2.90 gm/cm3")

plt.suptitle("Bouguer anomalyu comparison - ERG area")
plt.tight_layout()
plt.savefig("bouguer_anomaly_comparison.png", dpi=300, bbox_inches="tight")
plt.show()


# Difference map
df["difference"] = df["bouguer_290"] - df["bouguer_267"]

fig, ax = plt.subplots(figsize=(10, 8))

sc = ax.scatter(df["longitude"],
                df["latitude"],
                c=df["difference"],
                cmap="RdBu_r",
                s=10)

plt.colorbar(sc, ax=ax, label="Difference (mGal)")
ax.set_xlabel("longitude")
ax.set_ylabel("latitude")
ax.set_title("Difference 2.90 - 2.67 g/cm3")
plt.tight_layout()
plt.savefig("bouguer_difference.png", dpi=300, bbox_inches="tight")
plt.show()