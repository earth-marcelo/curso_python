station_names = ["est_01", "est_02", "est_03", "est_04", "est_05", "est_06", "est_07"]
bouguer = [-45.2, -38.7, -52.1, -41.3, -48.9, -35.6, -50.2]

for i in range(len(bouguer)):
    print(station_names[i], "->", bouguer[i], "mGal")