text = open("./values/2022-1", "r").read().split("\n\n")
text = sorted([sum(map(int, x.split("\n"))) for x in text])

print(text[-1])
print(sum(text[-3:]))
