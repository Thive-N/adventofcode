import sys
text = open("./values/2022-10", "r").read().splitlines()
# text = open("./values/2022-10", "r").readlines()
# text = text.split("\n")


x = 1
cl = 0
signals = list()


def cycle():
    global signals, x, cl

    if not (cl+1) % 40:
        print('\n', end='')
    elif abs(x-(cl % 40)) <= 1:
        print('▓', end='')
    else:
        print('░', end='')

    cl += 1

    if (cl - 20) % 40 == 0:
        signals.append(cl * x)


for instruction in text:
    cycle()
    if instruction.startswith("addx"):
        cycle()
        instruction = instruction.split()
        x += int(instruction[1])

print(sum(signals))
