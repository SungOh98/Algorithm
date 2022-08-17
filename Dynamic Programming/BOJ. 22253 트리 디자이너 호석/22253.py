'''
N * 10 dp 테이블을 생성.

'''

def dfs(graph, dp, start, weights):
    dp[start][weights[start]] = 1
    for node in graph[start]:
        if dp[node][weights[node]] == 0:
            dfs(graph, dp, node, weights)
            weight = weights[start]
            for i in range(weight, 10):
                dp[start][weight] += dp[node][i]
            for i in range(10):
                dp[start][i] += dp[node][i]


import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline
n = int(input())
array = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
dp = [[0] * 10 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph, dp, 1, array)
print(sum(dp[1]) % 1_000_000_007)