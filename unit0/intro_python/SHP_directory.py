# Let's take a look at the file we're given!
# For this, you'll be using the file directory.txt
# that's in the inputs folder. We're going to load
# the file into a list, then write some code to answer
# the questions below.

# Below each comment, write the code that answers that
# question. Fix the line below so that it loads
# "directory.txt" into a list called names.

file = open("directory.txt")

names = file.read().splitlines()

# Q0: What is the longest name?
longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name
print(longest)


# For the questions below, you'll need to make a
# frequency dictionary using people's first and last
# names.

# Q1: What's the most common first name?

first_names = [name.split(",")[1].split()[0] for name in names]
freqMap = {name:first_names.count(name) for name in first_names}
print(max(freqMap, key=freqMap.get))


# Q2: How many "unique" first names are there?
print(len(freqMap))
