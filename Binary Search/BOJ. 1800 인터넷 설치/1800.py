'''
인터넷 설치
1번 노드와 N번 노드를 연결하려고 하는데
각 노드별 연결 비용이 다르다.
또한 모든 노드가 연결될 필요는 없다.
K개의 간선에 대해서는 비용이 없다.
또한 비용을 받는 기준은 K개의 간선을 제외하고 연결한 간선 중 최대값 하나만 비용을 받기로 했다.
드는 비용의 최소값을 출력하시오, 만약 1번과 N번을 연결할 수 없다면 -1을 출력한다.
제한시간 : 2초
1 <= N <= 1000
1 <= P <= 10000
0 <= K <= 1000
1 <= price <= 1000000

dijkstra > O(P log N)


임의의 X 비용으로 N번까지 도달할 수 있는가?
있다면 > X를 줄여
없다면 > X를 늘려

어떻게 임의의 X비용으로 도달할 수 있는지 판단할까?
>> 1 ~ N까지의 경로에 임의의 X를 넘는 간선이 K개 이하라면 임의의 X 비용으로 도달할 수 있는 것이다!
따라서 다익스트라의 dist 배열에는 임의의 X를 넘는 간선의 개수를 저장하면 된다.
임의의 X를 넘는 간선의 개수를 최소로 N번 노드까지 도달할 수 있는지 판단!
'''

def dijkstra(x, count):
    # 시작 노드의 임의의 X를 넘는 간선의 개수는 0개
    count[1] = 0
    pq = []

    heapq.heappush(pq, [0, 1])

    while pq:
        cnt, node = heapq.heappop(pq)


        if cnt > count[node]:
            continue
        # node와 인접한 노드들의 cnt 갱신해주기

        for n_node, edge in graph[node]:
            # 간선의 비용이 임의의 X보다 크다면 1
            if edge > x:
                edge = 1
            # 간선의 비용이 임의의 X보다 작거나 같다면 0
            else:
                edge = 0
            # 만약 node를 거쳐서 n_node로 가는 경로에서 cnt의 개수가 더 작다면 갱신
            if count[n_node] > count[node] + edge:
                count[n_node] = count[node] + edge
                heapq.heappush(pq, [count[n_node], n_node])
    # 도달할 수 없다면 -1출력후 종료
    if count[n] == float('inf'):
        print(-1)
        exit(0)
    # n번 노드까지의 경로 중 임의의 X보다 큰 간선의 개수가 K보다 큰지 작은 지를 리턴
    else:
        return count[n] <= k


def parametric_search():
    start, end = 0, 1000000

    while start < end:
        mid = (start + end) // 2

        if dijkstra(mid, count[:]):
            end = mid

        else:
            start = mid + 1
    return (start + end) // 2


import heapq
n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
count = [float('inf')] * (n + 1)
for _ in range(p):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
print(parametric_search())