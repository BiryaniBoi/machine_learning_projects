



players = ["Wiggins", "Hield", "Schroder", "Green", "Santos", "Looney", "Anderson", "Waters III", "Moody", "Spencer", "Curry", "Jackson-Davis"]
points = [18, 7, 3, 10, 2, 9, 2, 5, 13, 4, 26, 0]

print(sum(points))
print(max(points))
print(min(points))
print(sorted(points, reverse=True))
players.pop(0)

for player in players:
    print(player)

my_file = open("mystery.txt")
print(my_file)
string_file = my_file.read()
print(string_file)
words = string_file.split()
print(words)

