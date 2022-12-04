text = open("./values/day4", "r").readlines()
text = [x.strip() for x in text]

s1 = s2 = 0

for x in text:
    a, b = x.split(",")
    a1, a2 = map(int, a.split("-"))
    b1, b2 = map(int, b.split("-"))

    a = set(range(a1, a2+1))
    b = set(range(b1, b2+1))

    if a.issubset(b) or b.issubset(a):
        s1 += 1

    if len(a.intersection(b)) > 0:
        s2 += 1

print(s1)
print(s2)
