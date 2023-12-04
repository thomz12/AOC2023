from aoc_helper import get_input
import re

def part1(input: str) -> str:
    lines = input.splitlines()
    total = 0
    for line in range(len(lines)):
        reds = all([int(val) <= 12 for val in re.findall("\\d+(?= red)", lines[line])])
        greens = all([int(val) <= 13 for val in re.findall("\\d+(?= green)", lines[line])])
        blues = all([int(val) <= 14 for val in re.findall("\\d+(?= blue)", lines[line])])
        if reds and greens and blues:
            total += line + 1
    return total

def part2(input: str) -> str:
    lines = input.splitlines()
    total = 0
    for line in range(len(lines)):
        reds = max([int(val) for val in re.findall("\\d+(?= red)", lines[line])])
        greens = max([int(val) for val in re.findall("\\d+(?= green)", lines[line])])
        blues = max([int(val) for val in re.findall("\\d+(?= blue)", lines[line])])
        total += reds * greens * blues
    return total

if __name__ == "__main__":
    input = get_input(2, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))