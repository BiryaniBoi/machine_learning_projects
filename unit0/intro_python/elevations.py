file = open("California_481x481.txt")

elevations = [[int(x) for x in line.split()] for line in file.read().splitlines()]

count = 0

for r in range(len(elevations)):
    for c in range(len(elevations[0])):
        if elevations[r][c] > 3500:
            count += 1
print(count)

locations = []

for r in range(len(elevations)):
    for c in range(len(elevations[0])):
        if elevations[r][c] > 3500:
            locations.append((r,c))
print(locations)