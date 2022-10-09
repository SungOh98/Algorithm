'''
1 <= N <= 1000 개의 컴퓨터
이들 중 몇개의 컴퓨터들은 서로 네트워크 연결이 되어 있음.
통신시 서로 연결되어 있는 컴퓨터끼리 통신할수도, 다른 컴퓨터를 거쳐서 통신할 수도 있음
가중치 존재

어느날 해커가 네트워크에 침입함.
네트워크 관리자가 모든 회선과 컴퓨터를 차단함.
관리자는 컴퓨터에  보안시스템을 설치하려함. >> 한대의 슈퍼 컴퓨터에만 설치 가능
한 컴퓨터가 공격을 받게 되면 네트워크를 통해 슈퍼컴퓨터에 이 사실이 전달됨
슈퍼컴퓨터는 네트워크를 이용하여 보안 패킷을 전송하는 방식이다.
다음과 같은 조건으로 네트워크를 복구함.

1. 해커가 다시 공격을 할 우려가 있으므로 최소 개수의 회선만을 복구해야함.
    >> 서로다른 두 컴퓨터 간에 통신이 가능하도록 복구해야함
2. 슈퍼 컴퓨터가 다른 컴퓨터들과 통신하는데 걸리는 최소 시간이 원래의 네트워크에서 통신하는데 걸리는 최소시간보다 커져서는 안된다.

양방향 간선이며 1번 컴퓨터가 슈퍼컴퓨터임.

그냥 다익스트라 + 경로 문제네
경로 저장 배열 생성후 담으면 될 듯
'''

import heapq


def dijkstra(path, distance, graph):
    distance[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        dist, node = heapq.heappop(pq)
        # 갱신 안된 경로라면 무시
        if distance[node] < dist:
            continue

        for adj_node, weight in graph[node]:
            if distance[adj_node] > dist + weight:
                distance[adj_node] = dist + weight
                heapq.heappush(pq, (distance[adj_node], adj_node))
                # 경로 기록
                path[adj_node] = node

def main_func():
    dist = [float('inf')] * (n + 1)
    path = [-1] * (n + 1)
    dijkstra(path, dist, graph)
    answer = []
    cnt = 0
    for i in range(1, n + 1):
        if path[i] != -1:
            answer.append((i, path[i]))
            cnt += 1
    print(cnt)
    for a, b in answer:
        print(a, b)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

main_func()


