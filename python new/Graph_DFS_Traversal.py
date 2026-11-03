g = {'A':['B','C'], 'B':['A','D','E'], 'C':['A','F'],
     'D':['B'], 'E':['B'], 'F':['C']}
def dfs(v, seen=None):
    if seen is None: seen = set()
    seen.add(v); print(v, end=" ")
    for u in g.get(v, []):
        if u not in seen: dfs(u, seen)
dfs('A')

