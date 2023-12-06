from aoc_helper import get_input
import re

def part1(input: str) -> str:
    lines = input.splitlines()
    maps = []
    for line in range(2, len(lines)):
        if not lines[line].strip():
            continue
        if ":" in lines[line]:
            maps.append([])
            continue
        maps[-1].append([int(num) for num in re.findall("\\d+", lines[line])])
    seeds = [int(seed) for seed in re.findall("\\d+", lines[0])]
    locations = []
    for seed in seeds:
        number = seed
        for map in maps:
            for ranges in map:
                if ranges[1] <= number < ranges[1] + ranges[2]:
                    number = ranges[0] + number - ranges[1]
                    break
        locations.append(number)
    return str(min(locations))


def part2(input: str) -> str:
    lines = input.splitlines()
    maps = []
    for line in range(2, len(lines)):
        if not lines[line].strip():
            continue
        if ":" in lines[line]:
            maps.append([])
            continue
        maps[-1].append([int(num) for num in re.findall("\\d+", lines[line])])
    seeds = [int(seed) for seed in re.findall("\\d+", lines[0])]
    location = 0
    while True:
        number = location
        for map in reversed(range(len(maps))):
            for ranges in maps[map]:
                if ranges[0] <= number < ranges[0] + ranges[2]:
                    number = ranges[1] + number - ranges[0]
                    break
        for seed in range(0, len(seeds), 2):
            if seeds[seed] <= number < seeds[seed] + seeds[seed+1]:
                return str(location)
        location += 1


if __name__ == "__main__":
    input = get_input(5, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))