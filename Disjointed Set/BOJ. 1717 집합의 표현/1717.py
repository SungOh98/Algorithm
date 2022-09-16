'''
Union - Find 기초문제
1 <= N <= 1_000_000
1 <= M <= 100_000

make_set : O(N)
find_set : O(logN)
union : O(logN)

M개의 쿼리에 대한 time complexity: O(MlogN)
'''
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(a, b, parent):
    a, b = find_parent(parent, a), find_parent(parent, b)

    if a > b:
        parent[b] = a
    else:
        parent[a] = b

def main_func():
    n, m = map(int, input().split())
    parents = [i for i in range(n + 1)]
    for _ in range(m):
        order, a, b = map(int, input().split())

        if order == 1:
            print("YES" if find_parent(parents, a) == find_parent(parents, b) else "NO")
        else:
            union(a, b, parents)

main_func()
