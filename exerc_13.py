# Reading a csv file
file_name = "bouguer.csv"

with open(file_name, "r") as file:
    lines = file.readlines()

# Remove the header
lines = lines[1:]

station_names = []
bouguer = []

for line in lines:
    parts = line.strip().split(",")
    station_names.append(parts[0])
    bouguer.append(float(parts[1]))

print("Stations loaded:", len(station_names))
for name, value in zip(station_names, bouguer):
    print(f"{name:8} {value:6.1f} mGal")