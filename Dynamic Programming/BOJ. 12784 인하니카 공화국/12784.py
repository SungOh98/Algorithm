'''
인하니카 공화국
1 <= N <= 1000개의 노드의 트리 존재
N - 1개의 가중치 간선이 주어짐
1번 노드로부터 모든 리프노드를 끊으려 한다
끊는 비용은 가중치임

최소 비용을 구하자

'''

def dfs(start, dp, visited, graph):
    visited[start] = True

    for node, edge in graph[start]:
        if not visited[node]:
            # dp 초기화 >> leaf 노드만 무한으로 설정하기 위한 것
            if dp[start] == float('inf'):
                dp[start] = 0


            dfs(node, dp, visited, graph)
            dp[start] += min(dp[node], edge)

TC = int(input())
for _ in range(TC):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dp = [float('inf')] * (n + 1)
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])
        graph[b].append([a, w])
    if n == 1:
        print(0)
    else:
        dfs(1, dp, [False] * (n + 1), graph)
        print(dp[1])