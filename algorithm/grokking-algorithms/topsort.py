


# 队列
def topsort(G):
    indegrees = {v : 0 for v in G}
    for li in G.values():
        for v in li:
            indegrees[v] += 1
    q = [v for v in G if indegrees[v] == 0]
    i = 0
    while i < len(q):
        for v in G[q[i]]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)
        i += 1
    if i == len(G):
        return q
    else:
        return None


G = {
    "C1": ["C3", "C8"],
    "C2": ["C3", "C4", "C5"],
    "C3": ["C4"],
    "C4": ["C6", "C7"],
    "C5": ["C6"],
    "C6": [],
    "C7": [],
    "C8": ["C9"],
    "C9": ["C7"],
}


print(topsort(G))

