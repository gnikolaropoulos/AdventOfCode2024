from collections import Counter

def solve_part_1(puzzle_input):
    all_left = []
    all_right = []
    for line in puzzle_input:
        left, right = line.split()
        left, right = int(left), int(right)
        all_left.append(left)
        all_right.append(right)
    all_left = sorted(all_left)
    all_right = sorted(all_right)
    answer = 0
    for l, r in zip(all_left, all_right):
        answer += abs(l-r)
    return answer


def solve_part_2(puzzle_input):
    all_left = []
    all_right = Counter()
    for line in puzzle_input:
        left, right = line.split()
        left, right = int(left), int(right)
        all_left.append(left)
        all_right[right] += 1
    all_left = sorted(all_left)
    score = 0
    for l in all_left:
        score += l * all_right.get(l,0)
    return score



def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line)
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")