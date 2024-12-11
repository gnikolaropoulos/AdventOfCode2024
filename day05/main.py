import functools


def solve_part_1(puzzle_input):
    answer = 0
    rules, updates = puzzle_input
    rules_cache = {}
    for x, y in rules:
        rules_cache[(x, y)] = -1
        rules_cache[(y, x)] = 1
    for update in updates:
        if is_update_ordered(rules_cache, update):
            answer += update[len(update) // 2]
    return answer


def is_update_ordered(cache, update):
    for i in range(len(update) - 1):
        key = (update[i], update[i + 1])
        if key in cache and cache[key] == 1:
            return False
    return True


def solve_part_2(puzzle_input):
    answer = 0
    rules, updates = puzzle_input
    rules_cache = {}
    for x, y in rules:
        rules_cache[(x, y)] = -1
        rules_cache[(y, x)] = 1
    for update in updates:
        if is_update_ordered(rules_cache, update):
            continue
        update.sort(key=functools.cmp_to_key(lambda x, y: compare(x, y, rules_cache)))
        answer += update[len(update) // 2]
    return answer


def compare(x, y, cache):
    return cache.get((x, y), 0)


def get_puzzle_input():
    is_reading_page_updates = False
    puzzle_input = open("input.txt").read().strip()
    rules = []
    updates = []
    for line in puzzle_input.splitlines():
        print(line)
        if line == "":
            is_reading_page_updates = True
            continue
        if not is_reading_page_updates:
            rule = list(map(int, line.split("|")))
            rules.append(rule)
        else:
            update = list(map(int, line.split(",")))
            updates.append(update)

    return (rules, updates)


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
