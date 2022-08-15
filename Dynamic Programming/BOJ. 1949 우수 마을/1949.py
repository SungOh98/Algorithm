'''
우수마을
1 <= N <= 10,000개의 마을
N-1개의 무방향 간선
우수 마을 선정 조건
몇 개의 마을을 우수마을로 선정함
1. 우수마을로 선정된 마을 주민 수의 총 합을 최대로 해야한다.
2. 우수마을끼리는 인접해 있을 수 없다.
3. 우수마을이 아닌 모든 마을은 적어도 하나이상의 우수 마을과 인접해 있어야 한다.

이 세 조건을 만족시키도록 우수 마을을 선정하고 우수 마을의 주민 수의 총합을 출력하자.
# dp[0]은 현재 노드를 선택한 경우
# dp[1]는 현재 노드를 선택하지 않은 경우 로 정의
점화식
현재 노드를 선택한 경우 >> 직전 노드를 선택하지 않은 부분 문제의 해답에서 가져오기
dp[0][i] = dp[1][k] + dp[0][i]
현재 노드를 선택하지 않을 경우 >> 직전 노드를 선택하던 안 선택하던 상관없이 최대값을 가져오기
dp[1][i] = max(dp[0][k], dp[1][k]) + dp[1][i]

k는 i와 인접한 노드임.
'''


def Top_Down(graph, array, dp, root):
    dp[0][root] = array[root]

    for k in graph[root]:
        if dp[0][k] == -1:
            Top_Down(graph, array, dp, k)
            dp[0][root] = dp[1][k] + dp[0][root]
            dp[1][root] = max(dp[1][k], dp[0][k]) + dp[1][root]
import sys
sys.setrecursionlimit(100000)
n = int(input())
array = [0] + list(map(int, input().split()))
# dp[1]은 현재 노드를 선택한 경우
# dp[2]는 현재 노드를 선택하지 않은 경우 로 정의

dp = []
dp.append([-1] * (n + 1))
dp.append([0] * (n + 1))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

Top_Down(graph, array, dp, 1)
print(max(dp[0][1], dp[1][1]))
