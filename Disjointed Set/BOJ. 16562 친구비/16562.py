'''
친구비
이준석은 0번 노드로 취급

랭크를 친구비로 설정 >> 친구비가 낮을 수록 높은 랭크
모든 노드를 0번 노드와 Union 하여 드는 비용이 주어진 비용과 비교하면 될 듯
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(a, b, parent, rank):
    a, b = find_parent(parent, a), find_parent(parent, b)

    if rank[a] > rank[b]:
        parent[a] = b
    else:
        parent[b] = a


def main_func():
    cost = 0
    for node in range(1, n + 1):
        parent_of_node = find_parent(parents, node)
        if parent_of_node != 0:
            cost += rank[parent_of_node]
            union(0, node, parents, rank)
    return cost if cost <= k else "Oh no"


import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
rank = [0] + list(map(int, input().split()))
parents = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    if find_parent(parents, a) != find_parent(parents, b):
        union(a, b, parents, rank)
print(main_func())
