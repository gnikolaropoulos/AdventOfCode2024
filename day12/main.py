from collections import deque


def solve_part_1(puzzle_input):
    regions = []
    seen = set()
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])
    for row in range(rows):
        for col in range(cols):
            if (row, col) in seen:
                continue
            seen.add((row, col))
            region = {(row, col)}
            q = deque([(row, col)])
            crop = puzzle_input[row][col]
            while q:
                cur_row, cur_col = q.popleft()
                for next_row, next_col in [
                    (cur_row - 1, cur_col),
                    (cur_row + 1, cur_col),
                    (cur_row, cur_col - 1),
                    (cur_row, cur_col + 1),
                ]:
                    if (
                        next_row < 0
                        or next_row >= rows
                        or next_col < 0
                        or next_col >= cols
                    ):
                        continue
                    if puzzle_input[next_row][next_col] != crop:
                        continue
                    if (next_row, next_col) in region:
                        continue
                    region.add((next_row, next_col))
                    q.append((next_row, next_col))
            seen |= region
            regions.append(region)
    return sum(len(region) * perimeter(region) for region in regions)


def perimeter(region):
    value = 0
    for row, col in region:
        value += 4
        for next_row, next_col in [
            (row - 1, col),
            (row + 1, col),
            (row, col - 1),
            (row, col + 1),
        ]:
            if (next_row, next_col) in region:
                value -= 1
    return value


def solve_part_2(puzzle_input):
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])

    regions = []
    seen = set()

    for row in range(rows):
        for col in range(cols):
            if (row, col) in seen:
                continue
            seen.add((row, col))
            region = {(row, col)}
            q = deque([(row, col)])
            crop = puzzle_input[row][col]
            while q:
                cur_row, cur_col = q.popleft()
                for next_row, next_col in [
                    (cur_row - 1, cur_col),
                    (cur_row + 1, cur_col),
                    (cur_row, cur_col - 1),
                    (cur_row, cur_col + 1),
                ]:
                    if (
                        next_row < 0
                        or next_col < 0
                        or next_row >= rows
                        or next_col >= cols
                    ):
                        continue
                    if puzzle_input[next_row][next_col] != crop:
                        continue
                    if (next_row, next_col) in region:
                        continue
                    region.add((next_row, next_col))
                    q.append((next_row, next_col))
            seen |= region
            regions.append(region)

    return sum(len(region) * sides(region) for region in regions)


def sides(region):
    corner_candidates = set()
    for r, c in region:
        for cr, cc in [
            (r - 0.5, c - 0.5),
            (r + 0.5, c - 0.5),
            (r + 0.5, c + 0.5),
            (r - 0.5, c + 0.5),
        ]:
            corner_candidates.add((cr, cc))
    corners = 0
    for cr, cc in corner_candidates:
        config = [
            (sr, sc) in region
            for sr, sc in [
                (cr - 0.5, cc - 0.5),
                (cr + 0.5, cc - 0.5),
                (cr + 0.5, cc + 0.5),
                (cr - 0.5, cc + 0.5),
            ]
        ]
        number = sum(config)
        if number == 1:
            corners += 1
        elif number == 2:
            if config == [True, False, True, False] or config == [
                False,
                True,
                False,
                True,
            ]:
                corners += 2
        elif number == 3:
            corners += 1
    return corners


def get_puzzle_input():
    grid = []
    with open("input.txt") as input_txt:
        for line in input_txt.readlines():
            grid.append(list(line.strip()))
    return grid


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
