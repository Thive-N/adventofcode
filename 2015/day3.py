text = open("./values/2015-3", "r").read()
#text = open("./values/2015-3", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

x, y = 0, 0
visited = set()
visited.add((x, y))
for c in text:
    if c == "^":
        y += 1
    elif c == "v":
        y -= 1
    elif c == ">":
        x += 1
    elif c == "<":
        x -= 1
    visited.add((x, y))

print(len(visited))

sx, sy = 0, 0
rx, ry = 0, 0
visited = set()
visited.add((sx, sy))
for i, c in enumerate(text):
    if i % 2 == 0:
        if c == "^":
            sy += 1
        elif c == "v":
            sy -= 1
        elif c == ">":
            sx += 1
        elif c == "<":
            sx -= 1
        visited.add((sx, sy))
    else:
        if c == "^":
            ry += 1
        elif c == "v":
            ry -= 1
        elif c == ">":
            rx += 1
        elif c == "<":
            rx -= 1
        visited.add((rx, ry))

print(len(visited))
