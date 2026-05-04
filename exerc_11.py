def calc_mean(values):
    return sum(values) / len(values)

bouguer = [-45.2, -38.7, -52.1, -41.3, -48.9, -35.6, -50.2]

result = calc_mean (bouguer)
print(f"Mean: {result:.1f} mGal")