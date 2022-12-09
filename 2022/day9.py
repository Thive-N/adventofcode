from lib.vector2d import Point

text = open("./values/2022-9", "r").read()
#text = open("./values/2022-9", "r").readlines()
text = text.split("\n")
#text = [x.split(" ") for x in text]
text = [x.strip().split() for x in text]

moves = {
    Point.from_tuple(0, 2): Point.from_tuple(0, 1),
    Point.from_tuple(0, -2): Point.from_tuple(0, -1),

    Point.from_tuple(1, 2): Point.from_tuple(1, 1),
    Point.from_tuple(1, -2): Point.from_tuple(1, -1),

    Point.from_tuple(2, -1): Point.from_tuple(1, -1),
    Point.from_tuple(2, 1): Point.from_tuple(1, 1),

    Point.from_tuple(-1, 2): Point.from_tuple(-1, 1),
    Point.from_tuple(-1, -2): Point.from_tuple(-1, -1),

    Point.from_tuple(-2, 1): Point.from_tuple(-1, 1),
    Point.from_tuple(-2, -1): Point.from_tuple(-1, -1),

    Point.from_tuple(2, 0): Point.from_tuple(1, 0),
    Point.from_tuple(-2, 0): Point.from_tuple(-1, 0),

    # cases for 10 rope
    Point.from_tuple(2, 2): Point.from_tuple(1, 1),
    Point.from_tuple(2, -2): Point.from_tuple(1, -1),

    Point.from_tuple(-2, 2): Point.from_tuple(-1, 1),
    Point.from_tuple(-2, -2): Point.from_tuple(-1, -1)
}

visited = set()
head = Point.zero()
tail = Point.zero()

for direction, steps in text:
    for _ in range(int(steps)):
        if direction == "U":
            head.x += 1
        elif direction == "D":
            head.y -= 1
        elif direction == "L":
            head.x -= 1
        elif direction == "R":
            head.x += 1
        if (max(abs(head.x-tail.x), abs(head.y-tail.y)) > 1):
            key = head - tail
            tail += moves[key]
        visited.add(tail)

print(len(visited))

visited = set()
points = [Point.zero() for _ in range(10)]
for direction, steps in text:
    for _ in range(int(steps)):
        if direction == "U":
            points[0].y += 1
        elif direction == "D":
            points[0].y -= 1
        elif direction == "L":
            points[0].x -= 1
        elif direction == "R":
            points[0].x += 1

        for i in range(1, 10):
            if (max(abs(points[i-1][0]-points[i][0]), abs(points[i-1][1]-points[i][1])) > 1):
                key = (points[i-1] - points[i])

                points[i] = points[i] + moves[key]
        visited.add(points[9])

print(len(visited))
