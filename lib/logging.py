from colorama import Fore, Style


def eprint(*args, sep=""):
    print(Fore.RED, "[e]", Style.RESET_ALL, sep.join(args))


def iprint(*args, sep=""):
    print(Fore.CYAN, "[i]", Style.RESET_ALL, sep.join(args))


def wprint(*args, sep=""):
    print(Fore.YELLOW, "[w]", Style.RESET_ALL, sep.join(args))
