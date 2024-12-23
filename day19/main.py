from functools import cache


def solve_part_1(puzzle_input):
    patterns, designs = puzzle_input
    maxlen = max(len(pattern) for pattern in patterns)

    @cache
    def can_obtain(design):
        if design == "":
            return True
        for i in range(min(len(design), maxlen) + 1):
            if design[:i] in patterns and can_obtain(design[i:]):
                return True
        return False

    return sum(1 if can_obtain(design) else 0 for design in designs)


def solve_part_2(puzzle_input):
    patterns, designs = puzzle_input
    maxlen = max(len(pattern) for pattern in patterns)

    @cache
    def all_possibilities(design):
        if design == "":
            return 1
        count = 0
        for i in range(min(len(design), maxlen) + 1):
            if design[:i] in patterns:
                count += all_possibilities(design[i:])
        return count

    return sum(all_possibilities(design) for design in designs)


def get_puzzle_input():
    patterns, designs = open("input.txt").read().split("\n\n")
    patterns = patterns.split(", ")
    designs = designs.split("\n")
    return patterns, designs


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
