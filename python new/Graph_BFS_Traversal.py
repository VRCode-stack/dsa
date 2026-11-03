from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}


def bfs(start):
    visited = [start]
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    print()


print("Graph (adjacency list):", graph)
source = int(input("Enter source vertex: "))
print("BFS traversal:", end=" ")
bfs(source)
