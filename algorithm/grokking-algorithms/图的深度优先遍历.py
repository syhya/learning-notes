
G = [{1, 2, 3},
     {0, 4, 6},
     {0, 3},        #2
     {0, 2, 4},     #3
     {1, 3, 5, 6},  #4
     {4, 7},        #5
     {1, 4},        #6
     {5}]           #7


# 递归dfs
def dfs(G, v, visited = set()):
    print(v, end=" ")
    visited.add(v)
    for u in G[v]:
        if u not in visited:
            dfs(G, u, visited)

# 迭代dfs : 栈+回溯法
def dfIter(G, v):
    visited =set()
    stack = [v]
    while stack: # 栈位空时结束
        u = stack.pop()
        if u not in visited:
            print(u, end=" ")
            visited.add(u)
            stack.extend(G[u])   #将u的领接元素压入stack中



dfs(G, 0)
print()
dfIter(G, 0)