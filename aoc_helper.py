import requests
import os.path

def get_input(day: int) -> str:
    filepath = "input/day" + str(day) + ".txt"
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
    request = requests.get("https://adventofcode.com/2023/day/" + str(day) + "/input", cookies = cookies)

    os.mkdir("input")
    file = open(filepath, "w")
    file.write(request.text)
    file.close()

    return request.text
