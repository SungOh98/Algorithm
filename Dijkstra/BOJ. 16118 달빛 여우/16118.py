'''
달빛 여우
달빛 늑대의 Dijkstra를 어떻게 처리할지가 관건 인 것 같다.
>> 각 노드당 2개의 dist 테이블을 정의하여 dist[i][0]에는 i번째 노드까지의 오는 최소 거리이 되, 바로 전 노드에서 거리 / 2 로 온 값
dist[i][1]에는 i번째 노드까지의 오는 최소거리이되 바로 전 노드에서 거리 * 2로 온 값을 저장해보자.

달빛 여우는 그냥 Dijkstra를 돌리고

각 노드당 달빛 여우의 dist[i] < 달빛 늑대의 min(dist[i])를 만족하는 노드의 개수를 세자.
내가 만들어본 예제 -> 늑대 다익스트라 알고리즘 도출하기 좋은 예제
5 6
1 2 3
1 3 8
2 3 1
2 4 22
4 5 8
3 5 4
42%에서 시간 초과 로직은 맞은 듯 한데..
'''
import sys
import heapq


def dijkstra(dist, graph):
    dist[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        weight, node = heapq.heappop(pq)
        if weight > dist[node]:
            continue

        for adj_node, edge in graph[node]:
            if dist[adj_node] > edge + weight:
                dist[adj_node] = edge + weight
                heapq.heappush(pq, (edge + weight, adj_node))
    return dist


def dijkstra_wolf(dist, graph):
    dist[1][1] = 0
    pq = []
    heapq.heappush(pq, (0, 1, 1))

    while pq:
        # idx가 0일 경우 다음 노드는 거리 / 2 만큼 감.
        weight, node, idx = heapq.heappop(pq)
        if weight > dist[node][idx]:
            continue

        if idx == 1:
            for adj_node, edge in graph[node]:
                if dist[adj_node][0] > weight + edge / 2:
                    dist[adj_node][0] = weight + edge / 2
                    heapq.heappush(pq, (weight + edge / 2, adj_node, 0))
        else:
            for adj_node, edge in graph[node]:
                if dist[adj_node][1] > weight + edge * 2:
                    dist[adj_node][1] = weight + edge * 2
                    heapq.heappush(pq, (weight + edge * 2, adj_node, 1))
    return dist


def answer(d1, d2):
    cnt = 0
    for i in range(1, n + 1):
        if d1[i] < min(d2[i]):
            cnt += 1
    return cnt


def main_func():
    dist_wolf = [[float('inf')] * 2 for _ in range(n + 1)]
    dist_rabbit = [float('inf')] * (n + 1)
    dist_wolf = dijkstra_wolf(dist_wolf, graph)
    dist_rabbit = dijkstra(dist_rabbit, graph)
    # print_board(dist_wolf)
    # print(dist_rabbit)
    return answer(dist_rabbit, dist_wolf)


def print_board(board):
    for i in board:
        print(i)
    print()



input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
# dist = dijkstra_wolf(dist, graph)
# print_board(dist)
print(main_func())
