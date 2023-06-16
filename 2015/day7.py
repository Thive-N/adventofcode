text = open("./values/2015-7", "r").read()
#text = open("./values/2015-7", "r").readlines()
#text = text.split("\n")
#text = [x.split(" ") for x in text]

wires = {}
cache = {}

for x in text.split("\n"):
    ins, out = x.split(" -> ")
    wires[out] = ins


def get_value(wire):
    if wire.isnumeric():
        return int(wire)

    if wires[wire].isnumeric():
        return int(wires[wire])

    if wire in cache:
        return cache[wire]

    ins = wires[wire].split(" ")

    if len(ins) == 1:
        ans = get_value(ins[0])
    elif len(ins) == 2:
        ans = ~get_value(ins[1])

    elif ins[1] == "AND":
        ans = get_value(ins[0]) & get_value(ins[2])
    elif ins[1] == "OR":
        ans = get_value(ins[0]) | get_value(ins[2])
    elif ins[1] == "LSHIFT":
        ans = get_value(ins[0]) << get_value(ins[2])
    elif ins[1] == "RSHIFT":
        ans = get_value(ins[0]) >> get_value(ins[2])

    cache[wire] = ans
    return ans


a = get_value("a")
cache = {}
wires["b"] = str(a)
print(a)
print(get_value("a"))
