from aoc_helper import get_input

nums = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

def part1(input: str) -> str:
    total = 0
    split = input.splitlines()
    for line in split:
        digits = [char for char in line if(char.isdigit())]
        total += int(digits[0] + digits[-1])
    return str(total)

def part2(input: str) -> str:
    total = 0
    split = input.splitlines()
    for line in split:
        firstDigit = 0
        lastDigit = 0
        for idx in range(len(line)):
            char = line[idx]
            if char.isdigit():
                firstDigit = int(char)
                break
            for number_idx in range(len(nums)):
                if line[idx:idx + len(nums[number_idx])] == nums[number_idx]:
                    firstDigit = number_idx + 1
                    break
            if firstDigit != 0:
                break
        for idx in range(len(line) - 1, -1, -1):
            char = line[idx]
            if char.isdigit():
                lastDigit = int(char)
                break
            for number_idx in range(0, len(nums)):
                if line[idx:idx + len(nums[number_idx])] == nums[number_idx]:
                    lastDigit = number_idx + 1
                    break   
            if lastDigit != 0:
                break

        total += int(str(firstDigit) + str(lastDigit))
    return str(total)

if __name__ == "__main__":
    input = get_input(1, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))