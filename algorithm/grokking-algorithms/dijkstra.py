import heapq

a, b, c, d, e, f = range(6)
G = {
    a: {b: 2, c: 1, d: 4, f: 10},
    b: {a: 2, c: 4, e: 3},
    c: {a: 1, b: 4, d: 2, f: 8},
    d: {a: 4,c: 2, e: 1},
    e: {b: 3, d: 1, f: 7},
    f: {a: 10, c: 8, e: 7},
}


def dijkstra(G, s):
    # D = {}, D[c], D[e]
    inf = float("inf")
    D = {v: inf for v in G}
    D[s] = 0
    P = {}
    S = {s}
    q = []

    v = s

    for _ in range(len(G)-1):
        for key, val in G[v].items():
            distance = D[v] + G[key][v]
            if D[key] > distance:
                D[key] = distance
                P[key] = v
                heapq.heappush(q, (distance, key))
        while q:
            _, v = heapq.heappop(q)
            if v not in S:
                S.add(v)
                break
        else:
            break

    return D, P


print(dijkstra(G, a))