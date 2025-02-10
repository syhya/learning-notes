G = [{1, 2, 3},
     {0, 4, 6},
     {0, 3},        #2
     {0, 2, 4},     #3
     {1, 3, 5, 6},  #4
     {4, 7},        #5
     {1, 4},        #6
     {5}]           #7

from collections import deque

def bfs(G ,v):
    q = deque([v])
    visited = {v}
    while q:
        u = q.popleft() # 出队一个元素
        print(u, end=" ")
        for w in G[u]:
            if w not in visited:
                q.append(w)
                visited.add((w))

bfs(G, 0)