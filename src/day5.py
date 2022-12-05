import re
text = open("./values/day5", "r").read()
# text = open("./values/day5", "r").readlines()
text = text.split("\n")
#text = [x.split(" ") for x in text]

stacks = [[] for x in range(9)]
for x in text:
    sn = 0
    if not x.startswith("["):
        break
    x = list(x)
    for i in range(1, 35, 4):
        if x[i] != " ":
            stacks[sn].append(x[i])

        sn += 1

stacks = [x[::-1] for x in stacks]

for line in text:
    if not line.startswith("move"):
        continue
    #temp = []
    c, f, t = re.findall('\d+', line)
    f = int(f) - 1
    t = int(t) - 1

    for i in range(int(c)):
        # temp.append(stacks[int(f)].pop())
        stacks[int(t)].append(stacks[int(f)].pop())
        # temp = temp[::-1]
        # for it in temp:
        #   stacks[int(t)].append(it)
for i in stacks:
    print(i[-1], end='')
