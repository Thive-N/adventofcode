from lib.logging import (eprint, iprint, wprint)
import os
import sys


def create_day(year: int, day: int) -> None:

    PYTHON_TEMPLATE = """text = open("./values/{0}-{1}", "r").read()
#text = open("./values/{0}-{1}", "r").readlines()
#text = text.split("\\n")
#text = [x.split(" ") for x in text]\n""".format(year, day)

    if not os.path.exists("./"+year):
        os.mkdir(year)
        iprint("creating folder ", year)

    if not os.path.exists("./values"):
        os.mkdir("values")
        iprint("creating values folder")

    PF = "./"+year+"/day"+day+".py"
    VF = "./values/"+year+"-"+day

    if not os.path.exists(PF):
        f = open(PF, "w")
        iprint("creating ", PF, " file")
        f.write(PYTHON_TEMPLATE)
        f.close()
        iprint("writing contents to ", PF)

    else:
        iprint(PF, " exists skipping file")

    if not os.path.exists(VF):
        open(VF, "x")
        iprint("creating ", VF, " file")
    else:
        iprint(VF, " exists skipping file")


def main():
    if len(sys.argv) < 2:
        eprint("Year not supplied")
        return

    elif len(sys.argv) < 3:
        eprint("Day not supplied")
        return

    if not sys.argv[1].isnumeric():
        eprint("Invalid format for year")
        return

    elif not sys.argv[2].isnumeric():
        eprint("Invalid format for day")
        return

    year = int(sys.argv[1])
    day = int(sys.argv[2])

    if 2015 > year or year > 2022:
        eprint("invalid year [", str(year), "]")
        return

    if 0 > day or day > 25:
        eprint("invalid day [", str(day), "]")
        return

    create_day(str(year), str(day))


if __name__ == "__main__":
    main()
