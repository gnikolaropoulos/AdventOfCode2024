import heapq


def solve_part_1(puzzle_input):
    rows = len(puzzle_input)
    cols = len(puzzle_input[0])

    for row in range(rows):
        for col in range(cols):
            if puzzle_input[row][col] == "S":
                start_row = row
                start_col = col
                break
        else:
            continue
        break

    pq = [(0, start_row, start_col, 0, 1)]
    seen = {(start_row, start_col, 0, 1)}

    while pq:
        cost, row, col, dr, dc = heapq.heappop(pq)
        seen.add((row, col, dr, dc))
        if puzzle_input[row][col] == "E":
            return cost
        for new_cost, next_row, next_col, next_direction_row, next_direction_column in [
            (cost + 1, row + dr, col + dc, dr, dc),
            (cost + 1000, row, col, dc, -dr),
            (cost + 1000, row, col, -dc, dr),
        ]:
            if puzzle_input[next_row][next_col] == "#":
                continue
            if (next_row, next_col, next_direction_row, next_direction_column) in seen:
                continue
            heapq.heappush(
                pq,
                (
                    new_cost,
                    next_row,
                    next_col,
                    next_direction_row,
                    next_direction_column,
                ),
            )


def solve_part_2(puzzle_input):
    pass


def get_puzzle_input():
    grid = [list(line.strip()) for line in open("input.txt")]

    return grid


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
