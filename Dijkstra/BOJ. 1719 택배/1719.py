# 노드, 간선 정보가 주어질 때 i번 노드에서 j번 노드로 최단 경로로 갈때, 제일먼저 가야하는 노드의 번호를 출력하시오
import heapq


def dijkstra(path, distance, start, graph, n):
    distance[start] = 0

    pq = []

    heapq.heappush(pq, [0, start])

    while pq:
        min_dist, min_node = heapq.heappop(pq)

        if min_dist > distance[min_node]:
            continue

        for node, weight in graph[min_node]:
            if distance[node] > distance[min_node] + weight:
                distance[node] = distance[min_node] + weight
                heapq.heappush(pq, [distance[node], node])

                path[node] = min_node

    for i in range(1, n + 1):
        if i == start:
            print("-", end=" ")
        else:
            print(get_first_node(path, i, start), end=" ")
    print()

def get_first_node(path, node, start):
    if path[node] == start:
        return node

    return get_first_node(path, path[node], start)

def print_answer():
    # O(N)
    for i in range(1, n + 1):
        # 얕은 복사해주기
        # O(Mlog N)
        dijkstra(path[:], distance[:], i, graph, n)
    # O(NM log N)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [float('inf')] * (n + 1)
path = [0] * (n + 1)
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
print_answer()