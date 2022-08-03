'''
희소 배열을 활용한 최소 공통 조상


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
def make_sparse_array(parent, distance):
    for j in range(1, 18):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]
    # 2^i 번쨰 부모까지의 거리를 저장한 거리 테이블
    for j in range(1, 18):
        for i in range(1, n + 1):
            distance[i][j] = distance[i][j - 1] + distance[parent[i][j - 1]][j - 1]

def LCA(a, b, parent, distance, depth_arr):
    answer = 0
    # 먼저 높이 맞추기
    min_depth = min(depth_arr[a], depth_arr[b])

    while depth_arr[a] > min_depth:
        # 깊이가 min_depth 보다 크거나 같은 2^i번째 부모를 만나면 그 부모로 자신을 바꾸기
        for i in range(17, -1, -1):
            if depth_arr[parent[a][i]] >= min_depth:
                # 거리도 추가
                answer += distance[a][i]
                a = parent[a][i]
                break
    while depth_arr[b] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parent[b][i]] >= min_depth:
                answer += distance[b][i]
                b = parent[b][i]
                break

    # 높이 맞춘 후 하나씩 올라가기.
    # 바로위의 부모가 같으면 멈추기
    while parent[a][0] != parent[b][0]:
        # 깊이가 낮은 부모부터 탐색하여 다른 부모가 나오면 바꾸기
        for i in range(17, -1, -1):
            if parent[a][i] != parent[b][i]:
                answer += distance[a][i]
                answer += distance[b][i]
                a, b = parent[a][i], parent[b][i]
                break

    if a != b:
        answer += distance[a][0] + distance[b][0]

    return answer

def main_func():
    depth_arr = [-1] * (n + 1)
    parents = [[0] * 18 for _ in range(n + 1)]
    dist_from_parents = [[0] * 18 for _ in range(n + 1)]
    dfs(parents, dist_from_parents, depth_arr, 0, 1)
    make_sparse_array(parents, dist_from_parents)
    # print_board(parents, 3)
    # print_board(dist_from_parents, 3)
    for a, b in nodes:
        print(LCA(a, b, parents, dist_from_parents, depth_arr))


import sys
sys.setrecursionlimit(40001)
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