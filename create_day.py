import os
import sys


def create_day(x: int):
    PYTHON_TEMPLATE = """text = open("./values/day{0}", "r").read()
#text = open("./values/day{0}", "r").readlines()
#text = text.split("\\n")
#text = [x.split(" ") for x in text]\n""".format(x)

    if not os.path.exists("./src"):
        os.mkdir("src")
        print("creating src folder")

    if not os.path.exists("./values"):
        os.mkdir("values")
        print("creating values")

    PF = "./src/day"+str(x)+".py"
    if not os.path.exists(PF):
        f = open(PF, "w")
        f.write(PYTHON_TEMPLATE)
        f.close()
    else:
        print(PF, " exists skipping")

    VF = "./values/day"+str(x)
    if not os.path.exists(VF):
        open(VF, "x")
    else:
        print(VF, " exists skipping")


def main():
    print(sys.argv)
    if not sys.argv[1].isnumeric():
        if sys.argv[1] == "all":
            for x in range(25):
                create_day(x+1)
            return
        else:
            print("invalid arg")
            return

    day = int(sys.argv[1])
    if 1 > day > 25:
        print("invalid day")
        return

    create_day(day)


if __name__ == "__main__":
    main()
