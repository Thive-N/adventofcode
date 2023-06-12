text = open("./values/2015-1", "r").read()
#text = open("./values/2015-1", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

print(text.count("(") - text.count(")"))
d = 0
for i, c in enumerate(text):
    if c == "(":
        d += 1
    elif c == ")":
        d -= 1
    if d == -1:
        print(i+1)
        break
