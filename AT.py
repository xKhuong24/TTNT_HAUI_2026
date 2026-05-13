graph = {
    "A": {"B": 2, "C": 4, "F": 6},
    "B": {},
    "C": {"D": 8, "E": 2},
    "D": {},
    "E": {},
    "F": {"G": 5, "H": 1},
    "G": {},
    "H": {}
}

def print_path_and_cost(start, goal, parent, g):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print("Đường đi:", ' -> '.join(path))
    print("C(p) = ", g[goal])

def AT(graph, start, goals):
    MO = [start]
    g = {start: 0}
    DONG = []
    parent = {}

    while MO:
        min_cost = float('inf')
        n = None
        for vertex in MO:
            cost = g[vertex] if vertex in g else float('inf')
            if cost < min_cost:
                min_cost = cost
                n = vertex

        if n in goals:
            print_path_and_cost(start, n, parent, g)
            return True

        MO.remove(n)
        DONG.append(n)

        for m in graph.get(n, {}):
            cost = graph[n][m]
            new_cost = g[n] + cost
            if m not in g or new_cost < g[m]:
                g[m] = new_cost
                parent[m] = n

            if m not in DONG and m not in MO:
                MO.append(m)

    return False

start = "A"
goals = ["D", "H"]
AT(graph, start, goals)