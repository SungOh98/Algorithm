def Dijkstra(path, start, distance, n, graph):
    # Priority Queue 생성
    priority_queue = []
    # 시작정점의 거리 0으로 설정
    distance[start] = 0
    # Priority Queue에 시작 정점 삽입: <시작정점까지의 거리, 노드 번호>
    heapq.heappush(priority_queue, [0, 0])
    # Priority Queue가 빌때까지 반복
    while priority_queue:
        # 최상위 원소를 pop하기
        dist, min_node = heapq.heappop(priority_queue)

        # pop한 원소의 거리가 갱신 되지 않았다면 무시
        if dist > distance[min_node]:
            continue
        # pop한 노드와 연결된 노드들의 시작노드로부터의 거리 갱신
        for node, weight in graph[min_node]:

            # min_node를 거쳐간 거리가 시작노드로부터 자신까지 바로 가는 거리보다 더 짧다면 거리 갱신
            if distance[min_node] + weight < distance[node]:
                distance[node] = distance[min_node] + weight
                # 갱신된 노드는 Priority Queue에 push
                heapq.heappush(priority_queue, [distance[node], node])
                # 경로 갱신
                path[node] = min_node
    # 경로 출력
    for i in range(n):
        print(f"{start}번 노드 부터 {i}번 노드까지의 최단 거리: {distance[i]}")
        print(f"{start}번 노드 부터 {i}번 노드까지의 최단 경로:", end=" ")
        print_path(i, path)
        print(i)
        print("---------------------------------------------")

def print_path(node, path):
    if path[node] == -1:
        return

    print_path(path[node], path)
    print(path[node], end=" > ")

'''
<입력>
8 14
0 1 8
0 4 9
0 5 11
4 5 3
4 1 6
1 2 10
4 2 1
5 7 8
5 6 8
6 4 12
2 3 2
6 3 5
7 6 7
3 7 4
0

'''
import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [float('inf')] * n
path = [-1] * n

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

start_node = int(input())
Dijkstra(path, start_node, distance, n, graph)