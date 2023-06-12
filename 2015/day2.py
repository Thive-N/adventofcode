text = open("./values/2015-2", "r").read()
#text = open("./values/2015-2", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

t = 0
for x in text.split("\n"):
    l, w, h = map(int, x.split("x"))
    a = [l*w, w*h, h*l]
    t += 2*sum(a) + min(a)
print(t)

t = 0
for x in text.split("\n"):
    l, w, h = map(int, x.split("x"))
    a = [l, w, h]
    t += 2*sum(sorted(a)[:2]) + l*w*h

print(t)
