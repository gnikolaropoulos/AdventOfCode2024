def solve_part_1(puzzle_input):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    top_grid, movements = puzzle_input
    map = []

    for line in top_grid.split("\n"):
        map.append(list(line.strip()))
    rows = len(map)
    cols = len(map[0])
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "@":
                start = (row, col)
                map[row][col] = "."
                break
        else:
            continue
        break

    current_row, current_col = start
    for movement in movements:
        if movement == "\n":
            continue
        direction = directions[movement]
        next_row, next_col = current_row + direction[0], current_col + direction[1]
        if map[next_row][next_col] == "#":
            continue
        elif map[next_row][next_col] == ".":
            current_row, current_col = next_row, next_col
        elif map[next_row][next_col] == "O":
            while map[next_row][next_col] == "O":
                next_row, next_col = next_row + direction[0], next_col + direction[1]
                if map[next_row][next_col] == "#":
                    continue
                elif map[next_row][next_col] == ".":
                    while (next_row, next_col) != (current_row, current_col):
                        map[next_row][next_col] = map[next_row - direction[0]][
                            next_col - direction[1]
                        ]
                        next_row, next_col = (
                            next_row - direction[0],
                            next_col - direction[1],
                        )
                    current_row, current_col = (
                        current_row + direction[0],
                        current_col + direction[1],
                    )

    return sum(
        100 * row + col
        for row in range(rows)
        for col in range(cols)
        if map[row][col] == "O"
    )


def solve_part_2(puzzle_input):
    directions = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    top_grid, movements = puzzle_input
    expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}

    map = [
        list("".join(expansion[char] for char in line))
        for line in top_grid.splitlines()
    ]

    # to_print = "\n".join("".join(row) for row in map)
    # print(to_print)

    rows = len(map)
    cols = len(map[0])
    for row in range(rows):
        for col in range(cols):
            if map[row][col] == "@":
                start = (row, col)
                break
        else:
            continue
        break

    for movement in movements:
        if movement == "\n":
            continue
        direction = directions[movement]
        targets = [(start[0], start[1])]
        go = True
        for current_row, current_col in targets:
            next_row, next_col = current_row + direction[0], current_col + direction[1]
            if (next_row, next_col) in targets:
                continue
            char = map[next_row][next_col]
            if char == "#":
                go = False
                break
            if char == "[":
                targets.append((next_row, next_col))
                targets.append((next_row, next_col + 1))
            if char == "]":
                targets.append((next_row, next_col))
                targets.append((next_row, next_col - 1))

        if not go:
            continue
        copy = [list(r) for r in map]
        map[start[0]][start[1]] = "."
        map[start[0] + direction[0]][start[1] + direction[1]] = "@"
        for target_row, target_col in targets[1:]:
            map[target_row][target_col] = "."
        for target_row, target_col in targets[1:]:
            map[target_row + direction[0]][target_col + direction[1]] = copy[
                target_row
            ][target_col]
        start = (
            start[0] + direction[0],
            start[1] + direction[1],
        )
    return sum(
        100 * row + col
        for row in range(rows)
        for col in range(cols)
        if map[row][col] == "["
    )


def get_puzzle_input():
    grid, movements = open("input.txt").read().strip().split("\n\n")
    return (grid, movements)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
