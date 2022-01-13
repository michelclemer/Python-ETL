import random
unordered = list(range(10)) * 1
ordered = []
i = 0

random.shuffle(unordered)

print(unordered)
lowest = unordered[0]

while len(unordered) > 0:
    if  unordered[i] < lowest:
        lowest = unordered[i]
    i += 1
    if i == len(unordered):
        ordered.append(lowest)
        unordered.remove(lowest)
        if unordered:
          lowest = unordered[0]
        i = 0

print(ordered)