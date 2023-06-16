text = open("./values/2015-8", "r").read()
# text = open("./values/2015-8", "r").readlines()
# text = text.split("\n")
# text = [x.split(" ") for x in text]

print("\n".join(list(map(str, map(sum, list(zip(
    *[(len(s) - len(eval(s)), 2+s.count('\\')+s.count('"'))for s in text.splitlines()])))))))
