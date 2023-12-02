from aoc_helper import get_input

def part1(input: str) -> str:
    split = input.splitlines()
    total = 0
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    for line in split:
        fail = False
        split_line = line.split(":")
        id = int("".join([char for char in split_line[0] if char.isdigit()]))
        for game in split_line[1].split(";"):
            reds = sum([int("".join([char for char in cubes if char.isdigit()])) for cubes in game.split(",") if cubes.find("red") != -1])
            greens = sum([int("".join([char for char in cubes if char.isdigit()])) for cubes in game.split(",") if cubes.find("green") != -1])
            blues = sum([int("".join([char for char in cubes if char.isdigit()])) for cubes in game.split(",") if cubes.find("blue") != -1])
            if reds > red_cubes or greens > green_cubes or blues > blue_cubes:
                fail = True
                break
        if not fail:
            total += id
    return total

def part2(input: str) -> str:
    split = input.splitlines()
    total = 0
    for line in split:
        split_line = line.split(":")
        red = []
        green = []
        blue = []
        for game in split_line[1].split(";"):
            red.append(sum([int("".join([char for char in cubes if char.isdigit()])) for cubes in game.split(",") if cubes.find("red") != -1]))
            green.append(sum([int("".join([char for char in cubes if char.isdigit()])) for cubes in game.split(",") if cubes.find("green") != -1]))
            blue.append(sum([int("".join([char for char in cubes if char.isdigit()])) for cubes in game.split(",") if cubes.find("blue") != -1]))
        total += max(red) * max(green) * max(blue)
    return total

if __name__ == "__main__":
    input = get_input(2, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))