def solve_part_1(puzzle_input):
    return sum(solve(num, 25, {}) for num in puzzle_input)


def solve_part_2(puzzle_input):
    return sum(solve(num, 75, {}) for num in puzzle_input)


def solve(num, time, cache):
    if (num, time) in cache:
        return cache[(num, time)]
    if time == 0:
        value = 1
    elif num == 0:
        value = solve(1, time - 1, cache)
    elif len(str(num)) % 2 == 0:
        str_num = str(num)
        left = int(str_num[: len(str_num) // 2])
        right = int(str_num[len(str_num) // 2 :])
        value = solve(left, time - 1, cache) + solve(right, time - 1, cache)
    else:
        value = solve(num * 2024, time - 1, cache)
    cache[(num, time)] = value
    return value


def get_puzzle_input():
    with open("input.txt") as input_txt:
        for line in input_txt:
            stones = [int(x) for x in line.split()]
    return stones


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
