def dfs(graph, dp, start):
    dp[start] = 1
    for node in graph[start]:
        if dp[node] == -1:
            dfs(graph, dp, node)
            dp[start] += dp[node]

import sys
sys.setrecursionlimit(10001)
input = sys.stdin.readline

n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [-1] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph, dp, r)
for _ in range(q):
    Query = int(input())
    print(dp[Query])
# print(dp)