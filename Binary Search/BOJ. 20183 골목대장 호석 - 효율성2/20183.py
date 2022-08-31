"""
1<= N <= 100,000 개의 노드
1 <= M <= 500,000 개의 간선
모든 간선에 자신의 분신을 두었다
간선을 통과하는 사람마다 수금한다.
수치침: A번노드에서 B번 노드까지의 경로상에 낸 돈의 최대값
수치심이 최소가 되도록 시작 노드에서 목표 노드까지 가려고 한다.

A번 노드에서 C원을 가지고 B번 노드까지 가려고 한다.
수치심의 최소값을 출력하자. C원으로 갈 수 없다면 -1을 출력하자.

파라메트릭 서치 문제
임의의 수치심 X로 A부터 B까지 갈 수 있는가?
갈 수 있다면 >> 줄여
갈 수 없다면 >> 늘려

결정함수 -> X이하의 간선들을 활용하여 A부터 B까지 가는 최소비용 경로를 구해야한다.
"""
import sys
import heapq


# O(M log N)
def dijkstra(x, start, end, money):
    costs = [float('inf')] * (n + 1)
    pq = []
    costs[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        cost, node = heapq.heappop(pq)

        if cost > costs[node]:
            continue

        for adj_node, adj_cost in graph[node]:
            # 수금 비용이 임의의 수치심 X보다 크다면 무시
            if adj_cost > x:
                continue
            if cost + adj_cost < costs[adj_node]:
                costs[adj_node] = cost + adj_cost
                heapq.heappush(pq, (costs[adj_node], adj_node))

    return costs[end] <= money


def parametric_search():
    start, end = 1, int(1e9) + 1
    while start < end:
        mid = (start + end) // 2

        if dijkstra(mid, s, e, c):
            end = mid
        else:
            start = mid + 1
    answer = (start + end) // 2
    return answer if answer <= int(1e9) else -1


input = sys.stdin.readline
n, m, s, e, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
print(parametric_search())
