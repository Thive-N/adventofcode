# text = open("./values/2022-8", "r").read()
text = open("./values/input.txt", "r").read()
# text = open("./values/2022-8", "r").readlines()
text = text.split("\n")
text = [list(map(int, list(x))) for x in text]


def is_visible(text, x, y):
    if x == 0 or x == len(text) - 1 or y == 0 or y == len(text) - 1:
        return True

    # 0..x..text.len
    taller = True
    for dx in range(0, x):
        if text[dx][y] >= text[x][y]:
            taller = False
            break

    if taller:
        return True

    taller = True
    for dx in range(x+1, len(text)):
        if text[dx][y] >= text[x][y]:
            taller = False
            break

    if taller:
        return True

    taller = True
    for dy in range(0, y):
        if text[x][dy] >= text[x][y]:
            taller = False
            break

    if taller:
        return True

    taller = True
    for dy in range(y+1, len(text[0])):
        if text[x][dy] >= text[x][y]:
            taller = False
            break

    if taller:
        return True

    return False


def scenic_score(text, x, y):
    ls = rs = us = ds = 0

    for dx in range(x-1, -1, -1):
        ls += 1
        if not text[x][y] > text[x][y]:
            break

    for dx in range(x+1, len(text)):
        rs += 1
        if not text[dx][y] > text[x][y]:
            break

    for dy in range(y-1, -1, -1):
        us += 1
        if not text[x][y-dy] > text[x][y]:
            break

    for dy in range(x+1, len(text)):
        ds += 1
        if not text[x][dy] > text[x][y]:
            break

    return ls * rs * us * ds


visible = 0
ss = 0

for x in range(len(text)):
    for y in range(len(text[x])):
        if is_visible(text, x, y):
            visible += 1
        ss = max(ss, scenic_score(text, x, y))

print(visible)
print(ss)
