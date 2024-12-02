def solve_part_1(reports):
    safe_reports = 0
    for report in reports:
        is_increasing = report == sorted(report) or report == sorted(
            report, reverse=True
        )
        is_valid = True
        for i in range(len(report) - 1):
            diff = abs(report[i] - report[i + 1])
            if not 1 <= diff <= 3:
                is_valid = False
        if is_increasing and is_valid:
            safe_reports += 1
    return safe_reports


def solve_part_2(reports):
    safe_reports = 0
    for r in reports:
        is_safe = False
        for j in range(len(r)):
            report = r[:j] + r[j + 1 :]
            is_increasing = report == sorted(report) or report == sorted(
                report, reverse=True
            )
            is_valid = True
            for i in range(len(report) - 1):
                diff = abs(report[i] - report[i + 1])
                if not 1 <= diff <= 3:
                    is_valid = False
            if is_increasing and is_valid:
                is_safe = True
                break
        if is_safe:
            safe_reports += 1
    return safe_reports


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(list(map(int, line.split())))
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
