'''
친구 네트워크

랭크를 자신을 루트로 하는 트리의 노드 개수로 설정하면 될 듯
다만 노드가 문자열이므로 딕셔너리로 rank와 parent를 표현해야함
>> 초기값 미리 입력하지 못한다. 따라서 입력과 동시에 해당 노드의 parent와 rank를 초기화 해줘야함.
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(a, b, parent, rank):
    a, b = find_parent(parent, a), find_parent(parent, b)

    if rank[a] >= rank[b]:
        rank[a] += rank[b]
        parent[b] = a
        print(rank[a])
    else:
        rank[b] += rank[a]
        parent[a] = b
        print(rank[b])


import sys

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n = int(input())
    parents = {}
    rank = {}
    for _ in range(n):
        a, b = input().split()
        # 초기 설정
        if a not in parents:
            parents[a] = a
            rank[a] = 1
        if b not in parents:
            parents[b] = b
            rank[b] = 1

        if find_parent(parents, a) != find_parent(parents, b):
            union(a, b, parents, rank)
        else:
            print(rank[find_parent(parents, a)])
