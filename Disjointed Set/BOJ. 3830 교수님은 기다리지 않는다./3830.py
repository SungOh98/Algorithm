'''
교수님은 기다리지 않는다.
2 <= N <= 100,000 개의 샘플 데이터
1 <= M <= 100,000 개의 쿼리가 주어지므로 각 쿼리를 최소 O(logN)에 해결해야 함
Union Find
'''

N = 0
parents = []
diff = []
rank = []


def make_set():
    global N, parents, diff, rank
    N = n
    parents = [i for i in range(N + 1)]
    diff = [0 for _ in range(N + 1)]
    rank = [0 for _ in range(N + 1)]


def union(a, b, w):
    RootA = find_set(a)
    RootB = find_set(b)
    diffFromRootA = get_diff(a)
    diffFromRootB = get_diff(b)

    if (rank[RootA] > rank[RootB]):
        diff[RootB] = w - (diffFromRootB - diffFromRootA)
        parents[RootB] = RootA
    elif (rank[RootA] < rank[RootB]):
        diff[RootA] = - w + (diffFromRootB - diffFromRootA)
        parents[RootA] = RootB
    else:
        diff[RootB] = w - (diffFromRootB - diffFromRootA)
        parents[RootB] = RootA
        rank[RootA] += 1


def get_diff(x):
    tmp = 0
    while (x != parents[x]):
        tmp += diff[x]
        x = parents[x]
    return tmp


def find_set(x):
    if (x != parents[x]):
        root = find_set(parents[x])
        if (root != parents[x]):
            diff[x] += diff[parents[x]]
        parents[x] = root
    return parents[x]


import sys

input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0: break
    make_set()
    for _ in range(m):
        query = input().split()
        if query[0] == '!':
            union(int(query[1]), int(query[2]), int(query[3]))
        else:
            a, b = int(query[1]), int(query[2])
            if (find_set(a) != find_set(b)):
                print("UNKNOWN")
            else:
                print(diff[b] - diff[a])
