'''
거리 구하기는 기본 문제니 pass
K번째 노드 번호 구하기.
내 알고리즘
1. 시작 노드와 끝 노드의 올라간 노드의 개수를 기록하며 최소 공통 조상을 찾는다. cnt: 시작점으로부터 최소 공통 조상의 순서, total : 시점 ~ 종점까지 노드 개수
2. cnt > k 일 경우 >> 시점을 k만큼 다시 올리기
cnt == k 일 경우 >> 최소 공통 조상 출력
cnt < k 일 경우 >> 종점을 total - k 만큼 올리기.
11
1 2 1
2 4 1
2 5 2
1 3 1
3 6 2
4 7 3
5 8 7
8 10 2
8 9 1
10 11 4
'''


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(start, depth):
    depth_arr[start] = depth
    for node, edge in graph[start]:
        if depth_arr[node] == -1:
            dfs(node, depth + 1)
            parents[node][0] = start
            distance[node][0] = edge

def make_sparse_table():
    dfs(1, 0)

    for j in range(1, 18):
        for i in range(1, n + 1):
            parents[i][j] = parents[parents[i][j - 1]][j - 1]
    for j in range(1, 18):
        for i in range(1, n + 1):
            distance[i][j] = distance[i][j - 1] + distance[parents[i][j - 1]][j - 1]

def LCA(s, e):
    s_cnt, e_cnt = 1, 1
    total_dist = 0
    min_depth = min(depth_arr[s], depth_arr[e])

    # 높이 먼저 맞추기
    while depth_arr[s] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parents[s][i]] >= min_depth:
                # 지나온 노드 개수 세기
                s_cnt += 2 ** i
                total_dist += distance[s][i]
                s = parents[s][i]
                break

    while depth_arr[e] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parents[e][i]] >= min_depth:
                # 지나온 노드 개수 세기
                e_cnt += 2 ** i
                total_dist += distance[e][i]
                e = parents[e][i]
                break

    while parents[s][0] != parents[e][0]:
        for i in range(17, -1, -1):
            if parents[s][i] != parents[e][i]:
                s_cnt += 2 ** i
                e_cnt += 2 ** i
                total_dist += distance[s][i] + distance[e][i]

                s, e = parents[s][i], parents[e][i]

                break

    if s == e:
        lca = s
    else:
        lca = parents[s][0]
        # s, e = parents[s][0], parents[e][0]
        total_dist += distance[s][0] + distance[e][0]
        s_cnt += 1
        e_cnt += 1
    e_cnt -= 1
    return s_cnt, s_cnt + e_cnt, total_dist, lca

def find_Kth(node, length):
    if length <= 0:
        return node
    else:
        for i in range(17, -1, -1):
            if 2 ** i <= length:
                return find_Kth(parents[node][i], length - 2 ** i)


n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [[0] * 18 for _ in range(n + 1)]
distance = [[float('inf')] * 18 for _ in range(n + 1)]
depth_arr = [-1] * (n + 1)
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])

make_sparse_table()
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    start, end = query[1], query[2]
    s_cnt, total_cnt, dist, lca = LCA(start, end)
    if query[0] == 1:
        print(dist)
    else:
        if query[3] == 0:
            print(start)
        elif query[3] == s_cnt:
            print(lca)
        elif query[3] < s_cnt:
            print(find_Kth(start, query[3] - 1))
        else:
            print(find_Kth(end, total_cnt - query[3]))