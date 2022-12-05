import re
text = open("./values/day5", "r").read()
# text = open("./values/day5", "r").readlines()
text = text.split("\n")
#text = [x.split(" ") for x in text]
stacks = []
stacks.append([])
stacks.append([])
stacks.append([])
stacks.append([])
stacks.append([])
stacks.append([])
stacks.append([])
stacks.append([])
stacks.append([])
stacks[0] = ["F", "D", "B", "Z", "T", "J", "R", "N"]
stacks[1] = ["R", "S", "N", "J", "H"]
stacks[2] = ["C", "R", "N", "J", "G", "Z", "F", "Q"]
stacks[3] = ["F", "V", "N", "G", "R", "T", "Q"]
stacks[4] = ["L", "T", "Q", "F"]
stacks[5] = ["Q", "C", "W", "Z", "B", "R", "G", "N"]
stacks[6] = ["F", "C", "L", "S", "N", "H", "M"]
stacks[7] = ["D", "N", "Q", "M", "T", "J"]
stacks[8] = ["P", "G", "S"]

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
