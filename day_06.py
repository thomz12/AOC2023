from aoc_helper import get_input
import re

def part1(input: str) -> str:
    lines = input.splitlines()
    totals = 1
    times = [int(time) for time in re.findall("\\d+", lines[0])]
    distances = [int(time) for time in re.findall("\\d+", lines[1])]

    for i in range(len(times)):
        total = 0
        for milliseconds in range(1, times[i]):
            distance = milliseconds * (times[i] - milliseconds)
            if distance > distances[i]:
                total += 1
        totals *= total

    return str(totals)

def part2(input: str) -> str:
    lines = input.splitlines()
    times = int("".join(re.findall("\\d+", lines[0])))
    distances = int("".join(re.findall("\\d+", lines[1])))
    total = 0
    for milliseconds in range(1, times):
        distance = milliseconds * (times - milliseconds)
        if distance > distances:
            total += 1

    return str(total)

if __name__ == "__main__":
    input = get_input(6, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))