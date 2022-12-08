import multiprocessing
text = open("./values/2022-8", "r").read()
text = text.split("\n")
text = [list(map(int, list(x))) for x in text]

maps = []

for x in range(len(text)):
    for y in range(len(text[x])):
        maps.append([x, y])


def is_visible(xy):
    x = xy[0]
    y = xy[1]
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


def scenic_score(xy):
    x = xy[0]
    y = xy[1]
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


def main():
    with multiprocessing.Pool() as pool:
        x1 = pool.map(is_visible, maps)
        x2 = pool.map(scenic_score, maps)
    yield sum(x1)
    yield max(x2)


if __name__ == '__main__':
    x = list(main())
    print(x[0])
    print(x[1])
