import os
import sys
from colorama import Fore, Style


def create_day(x: int):
    PYTHON_TEMPLATE = """text = open("./values/day{0}", "r").read()
#text = open("./values/day{0}", "r").readlines()
#text = text.split("\\n")
#text = [x.split(" ") for x in text]\n""".format(x)

    if not os.path.exists("./src"):
        os.mkdir("src")
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, " creating src folder")

    if not os.path.exists("./values"):
        os.mkdir("values")
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, " creating values folder")

    PF = "./src/day"+str(x)+".py"
    if not os.path.exists(PF):
        f = open(PF, "w")
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, "creating ", PF, " file")
        f.write(PYTHON_TEMPLATE)
        f.close()
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, "writing contents to ", PF)

    else:
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, " ", PF, " exists skipping file")

    VF = "./values/day"+str(x)
    if not os.path.exists(VF):
        open(VF, "x")
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, "creating ", VF, " file")
    else:
        print(Fore.LIGHTBLUE_EX, "[i]",
              Style.RESET_ALL, " ", VF, " exists skipping file")


def main():
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
