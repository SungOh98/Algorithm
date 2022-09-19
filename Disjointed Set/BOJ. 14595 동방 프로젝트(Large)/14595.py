'''
동방 프로젝트
벽을 허문 방끼리 union
>>
M번의 벽 허물기 이후에 집합의 개수 출력

2 <= N <= 1_000_000
0 <= M <= 5000

1000000
5000
1 1000000
1 1000000
...
...

위와 같은 입력이 주어질때 시간 초과주의 -> 점프하는 로직이 필요함
'''
import sys
sys.setrecursionlimit(1000001)
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

def answer(n, parent):
    cnt = 1
    for i in range(1, n):
        if find_parent(parent, i) != find_parent(parent, i + 1):
            cnt += 1
    return cnt

n = int(input())
m = int(input())
parents = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    # 점프하는 로직이 필요할 듯
    while find_parent(parents, a) != find_parent(parents, b):
        tmp = find_parent(parents, a) + 1
        union(a, b, parents)
        a = tmp
print(answer(n, parents))
# print(parents)