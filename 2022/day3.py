text = open("./values/2022-3", "r").readlines()
text = [x.strip() for x in text]

p = 0
for line in text:

    uniqa = set(line[:len(line)//2])
    uniqb = set(line[len(line)//2:])

    common = list(uniqa.intersection(uniqb))[0]

    p += ord(common) - 96 if common.islower() else ord(common) - 38

print(p)
p = 0
for i in range(0, len(text), 3):

    a = set(text[i])
    b = set(text[i+1])
    c = set(text[i+2])

    common = list(set.intersection(a, b, c))[0]

    p += ord(common) - 96 if common.islower() else ord(common) - 38
print(p)
