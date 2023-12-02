import requests
import os.path
import datetime

def get_input(day: int, year: int = 2023) -> str:
    filepath = "input/{}day{}.txt".format(year, day)
    if os.path.isfile(filepath):
        return open(filepath, "r").read()

    print("No input found, downloading input...")
    
    session = ""
    if os.path.isfile("session.txt"):
        session = open("session.txt", "r").read()
    else:
        print("No session.txt found! Add your session token in this file.")
        return ""

    cookies = {
        "session": session
    }
    request = requests.get("https://adventofcode.com/{}/day/{}/input".format(year, day), cookies = cookies)

    if not os.path.exists("input"):
        os.mkdir("input")
    file = open(filepath, "w")
    file.write(request.text)
    file.close()

    return request.text