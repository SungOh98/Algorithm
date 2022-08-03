'''
도로 네트워크
두 노드를 연결하는 경로 찾기 : 최소 공통 조상
입력의 크기가 매우 크므로 O(KN)으로 해결하지 못한다
따라서 희소 배열을 활용한다.
트리의 높이가 100,000 일 경우 희소배열의 한 행의 길이는 18로 설정하면 무리가 없다.
시간 복잡도 : O(K log 100,000)

'''


def print_board(board, idx):
    for i in board:
        print(i[:idx])
    print()


def dfs(parent, distance, depth_arr, depth, start):
    depth_arr[start] = depth

    for node, weight in graph[start]:
        if depth_arr[node] == -1:
            dfs(parent, distance, depth_arr, depth + 1, node)

            # backtrack 하면 서 바로위의 부모 정보와 바로위의 부모사이의 거리 정보를 저장한다.
            parent[node][0] = start
            distance[node][0] = weight


# 다이나믹 프로그래밍을 활용한 희소배열 완성하기 > 핵심
def make_sparse_array(parent, min_distance, max_distance):
    for j in range(1, 18):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]
    for j in range(1, 18):
        for i in range(1, n + 1):
            min_distance[i][j] = min(min_distance[i][j - 1], min_distance[parent[i][j - 1]][j - 1])
    for j in range(1, 18):
        for i in range(1, n + 1):
            max_distance[i][j] = max(max_distance[i][j - 1], max_distance[parent[i][j - 1]][j - 1])


def LCA(a, b, parent, min_dist, max_dist, depth_arr):
    # 먼저 높이 맞추기
    min_length, max_length = float('inf'), -1

    min_depth = min(depth_arr[a], depth_arr[b])

    while depth_arr[a] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parent[a][i]] >= min_depth:
                min_length = min(min_length, min_dist[a][i])
                max_length = max(max_length, max_dist[a][i])
                a = parent[a][i]
                break
    while depth_arr[b] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parent[b][i]] >= min_depth:
                min_length = min(min_length, min_dist[b][i])
                max_length = max(max_length, max_dist[b][i])
                b = parent[b][i]
                break

    # 올라가기
    while parent[a][0] != parent[b][0]:
        for i in range(17, -1, -1):
            if parent[a][i] != parent[b][i]:
                min_length = min(min_length, min_dist[a][i], min_dist[b][i])
                max_length = max(max_length, max_dist[a][i], max_dist[b][i])
                a = parent[a][i]
                b = parent[b][i]
                break
    if a != b:
        min_length = min(min_length, min_dist[a][0], min_dist[b][0])
        max_length = max(max_length, max_dist[a][0], max_dist[b][0])
    return f"{min_length} {max_length}"


def main_func():
    depth_arr = [-1] * (n + 1)
    parents = [[0] * 18 for _ in range(n + 1)]
    dist_from_parents = [[float('inf')] * 18 for _ in range(n + 1)]
    dfs(parents, dist_from_parents, depth_arr, 0, 1)
    max_dist_from_parents = [[-1] * 18 for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(18):
            if dist_from_parents[i][j] != float('inf'):
                max_dist_from_parents[i][j] = dist_from_parents[i][j]

    make_sparse_array(parents, dist_from_parents, max_dist_from_parents)
    # print_board(parents, 3)
    # print_board(dist_from_parents, 3)
    # print_board(max_dist_from_parents, 3)
    for a, b in nodes:
        print(LCA(a, b, parents, dist_from_parents, max_dist_from_parents, depth_arr))


import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])

nodes = []
k = int(input())
for _ in range(k):
    nodes.append(tuple(map(int, input().split())))
main_func()
