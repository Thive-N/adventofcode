text = open("./values/2015-5", "r").read()
#text = open("./values/2015-5", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

t = 0
s = 0
for x in text.split("\n"):
    if sum([x.count(y) for y in "aeiou"]) >= 3 and any([x[i] == x[i+1] for i in range(len(x)-1)]) and not any([x.count(y) for y in ["ab", "cd", "pq", "xy"]]):
        t += 1
    if any([x[i:i+2] in x[i+2:] for i in range(len(x)-2)]) and any([x[i] == x[i+2] for i in range(len(x)-2)]):
        s += 1
print(t)
print(s)
