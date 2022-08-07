def Dijkstra(path, start, visited, distance, n, graph):
    # 시작 정점의 거리 설정
    distance[start] = 0

    # 모든 노드 횟수만큼 반복 >> O(V)
    for _ in range(n):
        # 집합S에 포함되지 않은 노드들 중 시작 정점으로 부터의 거리가 가장짧은 노드를 선택
        min_dist, min_node = float('inf'), -1
        # O(V)
        for node in range(n):
            if not visited[node] and min_dist > distance[node]:
                min_dist = distance[node]
                min_node = node

        # 최소 길이 노드를 집합 S에 추가
        visited[min_node] = True

        # 집합 S에 포함되지 않고 최소길이 노드와 연결된 노드들의 시작노드로부터의 거리 갱신
        for node, weight in graph[min_node]:
            if not visited[node]:
                # min_node를 거쳐간 거리가 시작노드로부터 자신까지 바로 가는 거리보다 더 짧다면 거리 갱신
                if distance[min_node] + weight < distance[node]:
                    distance[node] = distance[min_node] + weight

                    # 경로 갱신
                    path[node] = min_node
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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [float('inf')] * n
path = [-1] * n
visited = [False] * n

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

start_node = int(input())
Dijkstra(path, start_node, visited, distance, n, graph)