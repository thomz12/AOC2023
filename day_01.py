from aoc_helper import get_input

puzzle_input = get_input(1)
split = puzzle_input.splitlines()

total = 0

for line in split:
    digits = [char for char in line if(char.isdigit())]
    total += int(digits[0] + digits[-1])
print(total)

total = 0

nums = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]

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
print(total)