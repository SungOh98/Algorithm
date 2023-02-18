

N = 0
parents = []
dist = []

def make_set(n):
    global N, parents, dist
    N = n
    parents = [i for i in range(N + 1)]
    dist = [0 for _ in range(N + 1)]



def find_set(x):
    if (x != parents[x]):
        root = find_set(parents[x])
        if (root != parents[x]):
            dist[x] += dist[parents[x]]
        parents[x] = root
    return parents[x]

def union(a, b):
    rootA = a
    rootB = find_set(b)
    tmp_dist = abs(a - b) % 1000
    dist[rootA] = get_dist(b) + tmp_dist
    parents[rootA] = rootB


def get_dist(x):
    tmp = 0
    while (x != parents[x]):
        tmp += dist[x]
        x = parents[x]
    return tmp

import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    n = int(input())
    make_set(n)
    while True:
        query = input().split()
        if query[0] == "O": break

        elif query[0] == "E":
            a = int(query[1])
            print(get_dist(a))

        else:
            a, b = int(query[1]), int(query[2])
            union(a, b)

