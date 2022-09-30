import sys
import math
'''
13
1 2
1 3
2 4
2 5
3 6
4 7
5 8
3 6
7 12
8 10
8 9
10 11
'''
LOG = math.ceil(math.log2(30000))


def init(parent, start, depth_arr, depth, tree):
    depth_arr[start] = depth
    for child in tree[start]:
        if depth_arr[child] == -1:
            init(parent, child, depth_arr, depth + 1, tree)
            parent[child][0] = start


def make_sparse(parent, n):
    for i in range(1, LOG + 1):
        for j in range(1, n + 1):
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def LCA(a, b, parent, depth):
    # 높이 먼저 맞추기
    min_depth = min(depth[a], depth[b])
    dist = 0
    while depth[a] > min_depth:
        for i in range(LOG, -1, -1):
            if depth[parent[a][i]] >= min_depth:
                dist += 1 << i
                a = parent[a][i]
                break
    while depth[b] > min_depth:
        for i in range(LOG, -1, -1):
            if depth[parent[b][i]] >= min_depth:
                dist += 1 << i
                b = parent[b][i]
                break
    # 바로 위의 부모가 같아질 때까지 반복
    while parent[a][0] != parent[b][0]:
        for i in range(LOG, -1, -1):
            if parent[a][i] != parent[b][i]:
                dist += (1 << i) * 2
                a = parent[a][i]
                b = parent[b][i]
                break

    if a != b:
        a, b = parent[a][0], parent[b][0]
        dist += 2
    return dist

def main_func():
    parent = [[0] * (LOG + 1) for _ in range(n + 1)]
    depth_arr = [-1] * (n + 1)
    init(parent, 1, depth_arr, 0, graph)
    make_sparse(parent, n)
    # for i in parent:
    #     print(i[:3])
    ans = 0
    for i in range(Q):
        ans += LCA(Query[i], Query[i + 1], parent, depth_arr)
    return ans

input = sys.stdin.readline
n = int(input())
Query = [1]
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
Q = int(input())
for _ in range(Q):
    Query.append(int(input()))
print(main_func())