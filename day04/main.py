def solve_part_1(puzzle_input):
    answer = 0
    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[0])):
            if puzzle_input[row][col] != "X":
                continue
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    if not (
                        0 <= row + 3 * dr < len(puzzle_input)
                        and 0 <= col + 3 * dc < len(puzzle_input[0])
                    ):
                        continue
                    if (
                        puzzle_input[row + dr][col + dc] == "M"
                        and puzzle_input[row + 2 * dr][col + 2 * dc] == "A"
                        and puzzle_input[row + 3 * dr][col + 3 * dc] == "S"
                    ):
                        answer += 1
    return answer


def solve_part_2(puzzle_input):
    answer = 0
    for row in range(1, len(puzzle_input) - 1):
        for col in range(1, len(puzzle_input[0]) - 1):
            if puzzle_input[row][col] != "A":
                continue
            corners = [
                puzzle_input[row - 1][col - 1],
                puzzle_input[row - 1][col + 1],
                puzzle_input[row + 1][col - 1],
                puzzle_input[row + 1][col + 1],
            ]
            corners_string = "".join(corners)
            if (
                corners_string == "MMSS"
                or corners_string == "MSSM"
                or corners_string == "SSMM"
                or corners_string == "SMMS"
            ):
                answer += 1
    return answer


def get_puzzle_input():
    puzzle_input = open("input.txt").read().strip().splitlines()

    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
