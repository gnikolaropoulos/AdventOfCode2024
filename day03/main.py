import re


def solve_part_1(puzzle_input):
    result = 0
    for i in range(len(puzzle_input)):
        if puzzle_input[i : i + 4] == "mul(":
            j = i + 4
            while puzzle_input[j] != ")":
                j += 1
            if puzzle_input[j - 1] not in [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]:
                continue
            try:
                x, y = map(int, re.findall(r"\d+", puzzle_input[i : j + 1]))
                result += x * y
            except:
                pass
    return result


def solve_part_2(puzzle_input):
    result = 0
    is_enabled = True
    for i in range(len(puzzle_input)):
        if puzzle_input[i : i + 4] == "do()":
            is_enabled = True
        if puzzle_input[i : i + 7] == "don't()":
            is_enabled = False
        if puzzle_input[i : i + 4] == "mul(":
            j = i + 4
            while puzzle_input[j] != ")":
                j += 1
            if puzzle_input[j - 1] not in [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
            ]:
                continue
            if not is_enabled:
                continue
            try:
                x, y = map(int, re.findall(r"\d+", puzzle_input[i : j + 1]))
                result += x * y
            except:
                pass
    return result


def get_puzzle_input():
    puzzle_input = open("input.txt").read().strip()

    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
