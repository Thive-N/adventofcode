import re
text = open("./values/2015-6", "r").read()
#text = open("./values/2015-6", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

actions1 = {
    'toggle': lambda x: 0 if x == 1 else 1,
    'turn on': lambda x: 1,
    'turn off': lambda x: 0
}
actions2 = {
    'toggle': lambda x: x + 2,
    'turn on': lambda x: x + 1,
    'turn off': lambda x: max(0, x - 1)
}

lights1 = [[0 for i in range(1000)] for j in range(1000)]
lights2 = [[0 for i in range(1000)] for j in range(1000)]

instructions = re.findall(
    "(toggle|turn on|turn off).(\d+),(\d+).through.(\d+),(\d+)", text)

for a, x1, y1, x2, y2 in instructions:
    coords = [(x, y)
              for x in range(int(x1), int(x2) + 1)
              for y in range(int(y1), int(y2) + 1)]

    for x, y in coords:
        lights1[x][y] = actions1[a](lights1[x][y])
        lights2[x][y] = actions2[a](lights2[x][y])

f1 = [val for sublist in lights1 for val in sublist]
f2 = [val for sublist in lights2 for val in sublist]
print(sum(f1))
print(sum(f2))
