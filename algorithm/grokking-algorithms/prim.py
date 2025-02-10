import heapq
def prim(G):


    n = len(G)
    v = 0
    # 集合
    s = {v}

    edges = []
    res = []

    for _ in range(n-1):
        for key, val in G[v].items():
            # 堆
            heapq.heappush(edges, (val, v, key))
        while edges:
            w, p, q = heapq.heappop(edges)
            if q not in s:
                s.add(q)
                res.append(((p, q), w))
                v = q
                break
        else:
            raise Exception("not connected graph")
    return res


G = [
    {1: 28, 5: 10},
    {0: 28, 2: 16, 6: 14},
    {1: 16, 3: 12},
    {2: 12, 4: 22, 6: 18},
    {3: 22, 5: 25, 6: 24},
    {0: 10, 4: 25},
    {1: 14, 3: 18, 4: 24},
]



print(prim(G))

r = prim(G)

total = sum([x[1] for x in r])
print("整个值为 %s" % total)





