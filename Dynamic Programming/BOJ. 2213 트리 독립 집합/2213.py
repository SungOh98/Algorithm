'''
우수마을과 똑같은데 경로 출력이 추가됨

'''

def dfs(start, graph, dp, path):
    dp[0][start] = array[start]
    path[0][start] += [start]
    for node in graph[start]:
        if dp[0][node] == -1:
            dfs(node, graph, dp, path)
            # i번째 노드를 포함한 경로
            # 가중치는 항상 양수기 때문에 더하는게 이득임
            dp[0][start] += dp[1][node]
            path[0][start] += path[1][node]
            # i번째 노드를 포함하지 않은 경로
            if dp[1][node] > dp[0][node]:
                dp[1][start] += dp[1][node]
                path[1][start] += path[1][node]

            else:
                dp[1][start] += dp[0][node]
                path[1][start] += path[0][node]



import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [[-1] * (n + 1), [0] * (n + 1)]

path = [
    [[] for _ in range(n + 1)],
    [[] for _ in range(n + 1)]
]
array = [0] + list(map(int, input().split()))
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1, graph, dp, path)
if dp[0][1] > dp[1][1]:
    print(dp[0][1])
    print(" ".join(map(str, sorted(path[0][1]))))
else:
    print(dp[1][1])
    print(" ".join(map(str, sorted(path[1][1]))))