class_names = ["Jad", "Charlie", "Adam", "Dylan", "Casey", "Oskar", "Sidney", "Sean", "Wilson", "Oliver", "Livia", "Henry"]
times = {n:[] for n in class_names}
for i in range(1880, 2025):
	with open('baby_names/yob' + str(i) + ".txt") as f:
		lines = f.read().splitlines()
		for line in lines:
			name, _, num = line.split(",")
			if name in class_names:
				if times[name] and times[name][-1][0] == i:
					times[name][-1]=(i, num + times[name][-1][1])
				else:
					times[name].append((i, num))

for name in times:
	f = open(name + ".txt", "w")
	for year, num in times[name]:
		f.write(str(year) + " " +str(num) + "\n")
	f.close()

