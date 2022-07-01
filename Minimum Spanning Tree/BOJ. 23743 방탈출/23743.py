'''
방탈출
1368번과 굉장히 비슷한 문제.
1368번은 노드 갯수가 300개여서 prime으로 쉽게 풀이가 가능했지만
23743번은 노드 갯수가 200000개 이므로 prime으로 AC 받을 수 없다.
elogv 의 kruskal로 접근해야한다.

0번 노드를 탈출구로 잡는다.
비상 탈출구를 건설하는데 걸리는 시간을 0번 노드와 연결한 엣지로 표현 한다.
0번 노드부터 n번 노드까지 모두 연결하는 MST를 만드는 비용을 구한다.
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def Kruskal(edges, parent):
    edges.sort(key=lambda x: x[2])
    cost = 0
    for a, b, w in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            cost += w
    return cost


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
edges = []
for _ in range(m):
    edges.append(tuple(map(int, input().split())))
tmp = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    edges.append((0, i, tmp[i]))

print(Kruskal(edges, parents))
