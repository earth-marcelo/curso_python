station_names = ["sta_01", "sta_02", "sta_03", "sta_04", "sta_05", "sta_06", "sta_07"]
bouguer = [-45.2, -38.7, -52.1, -41.3, -48.9, -35.6, -50.2]

for name, value in zip(station_names, bouguer):
    if value < -50.0:
        print(f"{name:8} -> {'strong anomaly':15} {value:6.1f} mGal")
    else:
        print(f"{name:8} -> {'weak anomaly':15} {value:6.1f} mGal")