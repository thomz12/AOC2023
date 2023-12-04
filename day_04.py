from aoc_helper import get_input

def part1(input: str) -> str:
    total = 0
    for line in input.splitlines():
        winning = [int(number) for number in line.split(":")[1].split("|")[0].split(" ") if number.isnumeric()]  
        owning = [int(number) for number in line.split(":")[1].split("|")[1].split(" ") if number.isnumeric()]
        total += int(2 ** (len(set(winning).intersection(owning)) - 1))
    return str(total)

def part2(input: str) -> str:
    current = 0
    lines = input.splitlines()
    amount = [1] * len(lines)
    for line in lines:
        winning = [int(number) for number in line.split(":")[1].split("|")[0].split(" ") if number.isnumeric()]  
        owning = [int(number) for number in line.split(":")[1].split("|")[1].split(" ") if number.isnumeric()]
        for i in range(len(set(winning).intersection(owning))):
            amount[current + i + 1] += 1 * amount[current]
        current += 1
    return sum(amount)
    
if __name__ == "__main__":
    input = get_input(4, 2023)
    print("part 1: {}".format(part1(input)))
    print("part 2: {}".format(part2(input)))