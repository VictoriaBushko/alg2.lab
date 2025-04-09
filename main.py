def read_graph():
    with open('input.txt') as f:
        n, m = map(int, f.readline().split())
        graph = {i: [] for i in range(1, n + 1)}
        for _ in range(m):
            u, v = map(int, f.readline().split())
            graph[u].append(v)
    return n, graph


def bfs(start, n, graph):
    visited = [False] * (n + 1)
    queue = [start]
    visited[start] = True
    count = 1

    while len(queue) > 0:
        node = queue[0]
        queue = queue[1:]

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count == n


def find_root_vertex(n, graph):
    for node in range(1, n + 1):
        if bfs(node, n, graph):
            return node
    return -1


n, graph = read_graph()
result = find_root_vertex(n, graph)

with open('output.txt', 'w') as f:
    f.write(str(result))
