'''
8:23 시작
물대기
n개의 논에 물을 대려고 한다.
방법 1. 직접 우물을 파는 것
방법 2. 이미 물을 대고 있는 다른 논으로부터 물을 끌어오는 방법

prime 으로 가자.
<my strategies>
1. 초기 거리 값을 우물을 파는데 필요한 비용으로 설정.
2. 프림 실행.
'''


def MST_Prime(dist):
    # 초기 출발 노드 설정 >> 그리디
    cost = 0
    visited = [False] * (n + 1)
    for _ in range(n):
        min_idx, min_v = -1, float('inf')
        for i in range(1, n + 1):
            if not visited[i] and dist[i] < min_v:
                min_idx, min_v = i, dist[i]

        cost += dist[min_idx]
        visited[min_idx] = True

        for node, weight in graph[min_idx]:
            if not visited[node] and dist[node] > weight:
                dist[node] = weight

    return cost



import sys
input = sys.stdin.readline

n = int(input())
distance = [float('inf')] * (n + 1)
graph = [[] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    distance[i] = int(input())

for i in range(1, n + 1):
    a = [0] + list(map(int, input().split()))
    for j in range(1, n + 1):
        if i != j:
            graph[i].append([j, a[j]])
# print(graph)
# print(distance)
print(MST_Prime(distance))