def print_table(table, idx):
    for i in table:
        print(i[:idx])
    print()


def make_sparse_table(parent, distance, graph):
    dfs(parent, distance, 1, [False] * (n + 1), graph)

    for j in range(1, 18):
        for i in range(1, n + 1):
            parent[i][j] = parent[parent[i][j - 1]][j - 1]

    for j in range(1, 18):
        for i in range(1, n + 1):
            distance[i][j] = distance[i][j - 1] + distance[parent[i][j - 1]][j - 1]

    # print_table(parent, 3)
    # print_table(distance, 3)


def find_closest_node(parent, distance, graph, node, energy):
    tmp = -1

    for i in range(17, -1, -1):
        if distance[node][i] <= energy:
            tmp = i

    if tmp == -1:
        return node

    else:
        return find_closest_node(parent, distance, graph, parent[node][tmp], energy - distance[node][tmp])


def dfs(parent, distance, start, visited, graph):
    visited[start] = True

    for node, edge in graph[start]:
        if not visited[node]:
            dfs(parent, distance, node, visited, graph)
            parent[node][0] = start
            distance[node][0] = edge


def main_func():
    parent = [[0] * 18 for _ in range(n + 1)]
    distance = [[float('inf')] * 18 for _ in range(n + 1)]
    make_sparse_table(parent, distance, graph)
    for i in range(1, n + 1):
        print(find_closest_node(parent, distance, graph, i, energies[i]))

import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline
n = int(input())
energies = [0] * (n + 1)
for i in range(1, n + 1):
    energies[i] = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])
    graph[b].append([a, w])
main_func()
'''
내가 생각해본 예제
13
58
6
4
9
3
22
55
31
2
10000
37
12
1
1 2 7
1 5 3
2 3 9
2 4 4
5 12 15
3 6 14
3 9 1
12 13 37
6 7 7
6 8 2
8 10 8
10 11 3
'''