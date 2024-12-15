import re


def solve_part_1(puzzle_input):
    robot_positions = []
    rows = 103
    columns = 101
    for px, py, vx, vy in puzzle_input:
        robot_positions.append(((px + vx * 100) % columns, (py + vy * 100) % rows))

    top_left = bottom_left = top_right = bottom_right = 0
    middle_row = (rows - 1) // 2
    middle_column = (columns - 1) // 2

    for robot_x, robot_y in robot_positions:
        if robot_x == middle_column or robot_y == middle_row:
            continue
        if robot_x < middle_column:
            if robot_y < middle_row:
                top_left += 1
            else:
                bottom_left += 1
        else:
            if robot_y < middle_row:
                top_right += 1
            else:
                bottom_right += 1

    return top_left * bottom_right * top_right * bottom_left


def solve_part_2(puzzle_input):
    rows = 103
    columns = 101
    min_safety_factor = 10000000000000000
    easter_egg_second = 0
    for second in range(rows * columns):
        robot_positions = []
        for px, py, vx, vy in puzzle_input:
            robot_positions.append(
                ((px + vx * second) % columns, (py + vy * second) % rows)
            )
            top_left = bottom_left = top_right = bottom_right = 0
            middle_row = (rows - 1) // 2
            middle_column = (columns - 1) // 2

        for robot_x, robot_y in robot_positions:
            if robot_x == middle_column or robot_y == middle_row:
                continue
            if robot_x < middle_column:
                if robot_y < middle_row:
                    top_left += 1
                else:
                    bottom_left += 1
            else:
                if robot_y < middle_row:
                    top_right += 1
                else:
                    bottom_right += 1
        safety_factor = top_left * bottom_right * top_right * bottom_left
        if safety_factor < min_safety_factor:
            min_safety_factor = safety_factor
            easter_egg_second = second
        print(second, safety_factor)
    return easter_egg_second


def get_puzzle_input():
    robots = []
    for line in open("input.txt").readlines():
        robots.append(tuple(map(int, re.findall(r"-?\d+", line))))
    return robots


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
