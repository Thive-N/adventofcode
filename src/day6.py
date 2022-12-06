text = open("./values/day6", "r").read()


def unique_n(n):
    for x in range(len(text)):
        if len(set(text[x:x+n])) == n:
            print(x + n)
            break


unique_n(4)
unique_n(14)
