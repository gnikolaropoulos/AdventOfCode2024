import re


def solve_part_1(puzzle_input):
    total = 0
    for block in puzzle_input:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            if ca <= 100 and cb <= 100:
                total += int(ca * 3 + cb)
    return total


def solve_part_2(puzzle_input):
    total = 0
    for block in puzzle_input:
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)
    return total


def get_puzzle_input():
    blocks = []
    for block in open("input.txt").read().split("\n\n"):
        blocks.append(block)
    return blocks


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
