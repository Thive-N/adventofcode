from typing import Union
import os
import requests
from bs4 import BeautifulSoup
from datetime import date
import json

config = json.load(open("config.json"))
cookies = {'session': config["sessionid"]}


def get_data(year: int, day: int) -> Union[str, int]:
    """downloads the data to the cache directory and returns it

    Args:
        day (int): the day you want to download
        year (int): which year you want to download from

    Returns:
        Union[str, int]: returns an int if an error has occured else returns a string
    """

    resq = requests.get(
        "https://adventofcode.com/{0}/day/{1}/input".format(year, day),
        cookies=cookies)

    if not resq.ok:
        code = resq.status_code
        print("error", code, "raised")
        if code == 404:
            print("This day is not available yet")
        elif code == 400:
            print("invalid credentials")
        return 0

    return resq.text.strip()


def submit(self, year: int, day: int, level: int, answer: str) -> int:
    """submit an answer for the advent of code

    Args:
        year (int): the year 
        day (int): the day
        level (int): the level
        answer (str): the answer

    Returns:
        int: a status code #! to be added
    """
    resq = requests.post(
        f"https://adventofcode.com/{year}/day/{day}/answer",
        cookies=cookies,
        data={"level": str(level), "answer": str(answer)})

    parsed = BeautifulSoup(resq.text, "html.parser")
    answerstat = parsed.article.text.lower().split(";")[0]

    if "not the right answer" in answerstat:
        print("Wrong answer")
        return 2

    elif "answer too recently" in answerstat:
        print("You gave an answer too recently")
        return 1

    elif "did you already complete it" in answerstat:
        print("You have already solved this")
        return 0

    elif "you need to actually provide an answer" in answerstat:
        print("provide a proper input")
        return 3


def submit_today_level1(answer: str, overridelevel1=False):
    """submits an answer for the advent of code using todays date and level 1


    Args:
        answer (str): the answer of the day
        overridelevel1 (bool, optional): if true sends to level 1 not 2. Defaults to False.
    """
    today = date.today()
    year = today.year()
    day = today.day()

    if overridelevel1:
        submit(year, day, 1, answer)
    else:
        submit(year, day, 2, answer)


def submit_today_level2(answer: str):
    submit_today_level1(overridelevel1=True)
