def read_graph_from_csv(filename='communication_wells.csv'):
    edges = []
    nodes = set()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            u, v, w = parts[0].strip(), parts[1].strip(), int(parts[2].strip())
            edges.append((w, u, v))
            nodes.add(u)
            nodes.add(v)
    return edges, nodes

def kruskal(edges, nodes):
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        parent[root_y] = root_x
        return True

    for node in nodes:
        parent[node] = node

    edges.sort()
    mst_weight = 0
    mst_edges = 0

    for weight, u, v in edges:
        if union(u, v):
            mst_weight += weight
            mst_edges += 1
            if mst_edges == len(nodes) - 1:
                break

    if mst_edges != len(nodes) - 1:
        return -1

    return mst_weight
