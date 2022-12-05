import re
import copy
text = open("./values/day5", "r").read()
text = text.split("\n")

stacks1 = [[] for x in range(9)]
for x in text:
    sn = 0
    if not x.startswith("["):
        break
    x = list(x)
    for i in range(1, 35, 4):
        if x[i] != " ":
            stacks1[sn].append(x[i])

        sn += 1

stacks1 = [x[::-1] for x in stacks1]
stacks2 = copy.deepcopy(stacks1)

for line in text:
    if not line.startswith("move"):
        continue
    c, f, t = re.findall('\d+', line)
    f = int(f) - 1
    t = int(t) - 1

    temp = []
    for i in range(int(c)):
        temp.append(stacks2[f].pop())

        stacks1[int(t)].append(stacks1[int(f)].pop())

    temp.reverse()
    for it in temp:
        stacks2[int(t)].append(it)


print("".join([x[-1] for x in stacks1]))
print("".join([x[-1] for x in stacks2]))
