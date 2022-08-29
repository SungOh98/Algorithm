'''
9 5
-1 1 2 3 4 2 6 6 7
2 2
3 4
6 3
5 6
7 1
ans:0 2 6 6 12 5 6 5 6

'''
def dfs(node, plus):
    compliments[node] += plus
    for child in graph[node]:
        dfs(child, compliments[node])

import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    graph[parents[i]].append(i)
compliments = [0] * (n + 1)
for _ in range(m):
    a, w = map(int, input().split())
    compliments[a] += w

# print(compliments)
dfs(1, compliments[1])
print(*compliments[1:], sep=" ")