def solve_part_1(puzzle_input):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])
    starting_pos = (0, 0)
    for i in range(rows):
        for j in range(cols):
            if puzzle_input[i][j] == "^":
                starting_pos = (i, j)
                break

    row, col = starting_pos
    dir = 0  # up
    seen = set()
    while True:
        seen.add((row, col))
        d_row, d_col = directions[dir]
        next_row, next_col = row + d_row, col + d_col
        if not (0 <= next_row < rows and 0 <= next_col < cols):
            break
        if puzzle_input[next_row][next_col] == "#":
            dir = (dir + 1) % 4
        else:
            row = next_row
            col = next_col
    return len(seen)


def solve_part_2(puzzle_input):
    loops = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])
    starting_pos = (0, 0)
    for i in range(rows):
        for j in range(cols):
            if puzzle_input[i][j] == "^":
                starting_pos = (i, j)
                break

    for i in range(rows):
        for j in range(cols):
            row, col = starting_pos
            dir = 0  # up
            seen = set()
            while True:
                if (row, col, dir) in seen:
                    loops += 1
                    break
                seen.add((row, col, dir))
                d_row, d_col = directions[dir]
                next_row, next_col = row + d_row, col + d_col
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    break
                if (
                    puzzle_input[next_row][next_col] == "#"
                    or next_row == i
                    and next_col == j
                ):
                    dir = (dir + 1) % 4
                else:
                    row = next_row
                    col = next_col
    return loops


def get_puzzle_input():
    grid = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            grid.append(line.strip())
    return grid


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
