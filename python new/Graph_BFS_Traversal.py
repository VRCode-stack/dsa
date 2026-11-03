from collections import deque
g = {'A':['B','C'], 'B':['A','D','E'], 'C':['A','F'],
     'D':['B'], 'E':['B'], 'F':['C']}
def bfs(start):
    seen, q = {start}, deque([start])
    while q:
        v = q.popleft(); print(v, end=" ")
        for u in g.get(v, []):
            if u not in seen: seen.add(u); q.append(u)
bfs('A')
