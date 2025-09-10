from collections import deque

def shortest_path(n, edges, start, end):
    if start == end:
        return 0

    # adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q = deque([(start, 0)])
    seen = {start}

    while q:
        u, d = q.popleft()
        for v in adj[u]:
            if v == end:
                return d + 1
            if v not in seen:
                seen.add(v)
                q.append((v, d + 1))

    return -1

print(shortest_path(5, [(0,1),(0,2),(1,3),(2,3),(3,4)], 0, 4))  # 3
print(shortest_path(3, [(0,1),(1,2)], 0, 2))  # 2
print(shortest_path(4, [(0,1),(1,2)], 2, 3))  # -1
print(shortest_path(1, [], 0, 0))             # 0
print(shortest_path(2, [], 0, 1))             # -1
