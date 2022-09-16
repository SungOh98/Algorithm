'''
여행 가자

여행 계획에 속한 도시들이 모두 연결되어 있는 그래프에 속하면 됨.
>> 모두 같은 집합인지 확인해야할듯
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(a, b, parent):
    a, b = find_parent(parent, a), find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
parents = [i for i in range(n + 1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        a, b = i + 1, j + 1

        if tmp[j] == 1 and find_parent(parents, a) != find_parent(parents, b):
            union(a, b, parents)

plan = list(map(int, input().split()))
answer = "YES"
for i in range(m - 1):
    if find_parent(parents, plan[i]) != find_parent(parents, plan[i + 1]):
        answer = "NO"
        break
print(answer)
