import hashlib
text = open("./values/2015-4", "r").read()
#text = open("./values/2015-4", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

i = 0
while True:
    if hashlib.md5((text + str(i)).encode()).hexdigest()[:5] == "00000":
        print(i)
        break
    i += 1
i = 0
while True:
    if hashlib.md5((text + str(i)).encode()).hexdigest()[:6] == "000000":
        print(i)
        break
    i += 1
