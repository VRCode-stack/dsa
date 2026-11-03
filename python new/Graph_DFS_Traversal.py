graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}


def dfs(v, visited):
    visited.append(v)
    print(v, end=" ")
    for neighbour in graph[v]:
        if neighbour not in visited:
            dfs(neighbour, visited)


print("Graph (adjacency list):", graph)
source = int(input("Enter source vertex: "))
print("DFS traversal:", end=" ")
dfs(source, [])
print()
