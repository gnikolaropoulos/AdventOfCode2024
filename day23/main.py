def solve_part_1(puzzle_input):
    graph = {}
    for x, y in puzzle_input:
        if x not in graph:
            graph[x] = set()
        if y not in graph:
            graph[y] = set()
        graph[x].add(y)
        graph[y].add(x)

    sets_of_three = set()

    for x in graph:
        for y in graph[x]:
            for z in graph[y]:
                if x != z and x in graph[z]:
                    sets_of_three.add(tuple(sorted([x, y, z])))

    return len([s for s in sets_of_three if any(node.startswith("t") for node in s)])


def solve_part_2(puzzle_input):
    graph = {}
    for x, y in puzzle_input:
        if x not in graph:
            graph[x] = set()
        if y not in graph:
            graph[y] = set()
        graph[x].add(y)
        graph[y].add(x)

    all_sets = set()

    def find_max_set(node, visited_nodes):
        key = tuple(sorted(visited_nodes))
        if key in all_sets:
            return
        all_sets.add(key)
        for neighbor in graph[node]:
            if neighbor in visited_nodes:
                continue
            if not (visited_nodes <= graph[neighbor]):
                continue
            find_max_set(neighbor, visited_nodes | {neighbor})

    for node in graph:
        find_max_set(node, {node})

    return ",".join(sorted(max(all_sets, key=len)))


def get_puzzle_input():
    edges = [line.strip().split("-") for line in open("input.txt")]

    return edges


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
