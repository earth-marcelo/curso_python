import math

def calc_stats(values):
    mean = sum(values) / len(values)
    minimum = min(values)
    maximum = max(values)
    squared_diff = 0
    for valor in values:
        squared_diff = squared_diff + (valor - mean)**2
    std = math.sqrt(squared_diff / len(values)) 
    
    return mean, minimum, maximum, std

# Reading the file
with open("bouguer.csv", "r") as file:
    lines = file.readlines()

lines = lines[1:]

station_names = []
bouguer = []

for line in lines:
    parts = line.strip().split(",")
    station_names.append(parts[0])
    bouguer.append(float(parts[1]))

# Statistics
mean, minimum, maximum, std = calc_stats(bouguer)
print(f"{'Mean:':19} {mean:6.1f} mGal")
print(f"{'Minimum:':19} {minimum:6.1f} mGal")
print(f"{'Maximum:':19} {maximum:6.1f} mGal")
print(f"{'Standard deviation:':19} {std:6.1f} mGal")
