from collections import defaultdict

def has_cycle(n, edges):
    # build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    seen = set()

    def dfs(node, parent):
        seen.add(node)
        for nxt in adj[node]:
            if nxt not in seen:
                if dfs(nxt, node):
                    return True
            elif nxt != parent:
                return True
        return False

    # check every component
    for i in range(n):
        if i not in seen:
            if dfs(i, -1):
                return True
    return False

print(has_cycle(5, [(0,1),(1,2),(2,3),(3,4),(4,0)]))  # True
print(has_cycle(3, [(0,1),(1,2)]))                    # False
print(has_cycle(4, [(0,1),(1,2),(2,0)]))              # True

# edge cases
print(has_cycle(3, []))                               # False
print(has_cycle(2, [(0,1),(0,1)]))                    # True
