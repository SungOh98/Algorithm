'''
사회망 서비스
사람은 노드
엣지는 친구관계
친구관계 그래프를 활용하면 사회망 서비스에서 어떤 새로운 아이디어가 전파되는 과정을 이해하는데 도움이된다.
새로운 아이디어를 먼저 받아들인 사람 : 얼리 어답터
얼리 어답터가 아닌 사람은 자신의 모든 친구가 얼리 어답터일 경우 아이디어를 받아들임
가능한 최소의 얼리어답터를 가지고 모든 사람이 아이디어를 받아들이게 하는 경우를 찾자
그래프가 트리인 경우에만 고려해보자

친구 관계 트리가 주어졌을 때 모든 사람이 새로운 아이디어를 받아들이기 위한 최소 얼리 어답터의 수를 구해보자.
1 <= N <= 1,000,000

트리, 경우의 수가 매우 많다 >> 트리 DP 의심
트리구조에서는 최적 부분 구조가 당연하다.
1. 용어 정의
dp[0][i] 는 i번째 노드가 얼리어답터 인 경우 i번째 노드까지의 최소 얼리 어답터 수
dp[1][i] 는 i번째 노드가 얼리 어답터가 아닌 경우 i번째 노드까지의 최소 얼리 어답터 수
2. 점화식
dp[0][i] = dp[0][i] + min(dp[0][k], dp[1][k]) : I번째 노드가 얼리 어답터 인경우 자식은 얼리 어답터이든 아니든 상관없으므로 최소값을 취한다
dp[1][i] = dp[1][i] + dp[0][k] : i번째 노드가 얼리 어답터가 아닌 경우 자식은 무조건 얼리 어답터 여야한다.
'''
def dfs(dp, start, graph):
    dp[0][start] = 1

    for node in graph[start]:
        if dp[0][node] == -1:
            dfs(dp, node, graph)
            dp[0][start] = dp[0][start] + min(dp[0][node], dp[1][node])
            dp[1][start] = dp[1][start] + dp[0][node]

import sys
sys.setrecursionlimit(1000001)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
dp = [[-1] * (n + 1), [0] * (n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(dp, 1, graph)
print(min(dp[0][1], dp[1][1]))