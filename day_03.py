from aoc_helper import get_input

def part1(input: str) -> str:
    split = input.split()
    total = 0
    for y in range(len(split)):
        skip = False
        for x in range(len(split[y])):
            if skip:
                if not split[y][x].isdigit():
                    skip = False
                continue
            if split[y][x].isdigit():
                number = "".join([char for char in split[y][x:x+3] if char.isdigit()])
                has_symbol = False
                min_x = max(0, min(x - 1, len(split[y])))
                min_y = max(0, min(y - 1, len(split)))
                max_x = max(0, min(x + len(number) + 1, len(split[y])))
                max_y = max(0, min(y + 2, len(split)))
                for bx in range(min_x, max_x):
                    for by in range(min_y, max_y):
                        if not split[by][bx].isdigit() and split[by][bx] != ".":
                            has_symbol = True
                if has_symbol:
                    total += int(number)
                skip = True
    return str(total)

def part2(input: str) -> str:
    split = input.split()
    total = 0
    for y in range(len(split)):
        for x in range(len(split[y])):
            if split[y][x] == "*":
                min_x = max(0, min(x - 1, len(split[y])))
                min_y = max(0, min(y - 1, len(split)))
                max_x = max(0, min(x + 2, len(split[y])))
                max_y = max(0, min(y + 2, len(split)))
                nums = []
                for bx in range(min_x, max_x):
                    for by in range(min_y, max_y):
                        if split[by][bx].isdigit():
                            number = split[by][bx]
                            for pos in range(bx + 1, bx + 3):
                                if not split[by][pos].isdigit():
                                    break
                                number += split[by][pos]
                            for neg in range(1, 3):
                                if not split[by][bx - neg].isdigit():
                                    break
                                number = split[by][bx - neg] + number
                            if not int(number) in nums:
                                nums.append(int(number))
                if len(nums) == 2:
                    total += nums[0] * nums[1]
    return str(total)

if __name__ == "__main__":
    input = get_input(3, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))