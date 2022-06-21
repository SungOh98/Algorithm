'''
문명
문명의 발상지로 부터 bfs 돌리기
새로 큐에 추가된 좌표들에 대해 union
통합 확인

bfs를 수행하면서 방문 처리
>> union은 방문 처리 된 곳만 union

'''
from collections import deque


# find_set
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union
def union(parent, a, b):
    a, b = find_parent(parent, a), find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 네 방향을 살펴 주위의 문명에 union 시키는 함수
def adjacent_union(y, x, visit, parent):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and visit[ny][nx]:
            if find_parent(parent, ny * n + nx) != find_parent(parent, y * n + x):
                union(parent, ny * n + nx, y * n + x)

# 문명이 모두 합쳐 졌는지 확인하는 함수
def check_sets(civils, parent):
    for i in range(1, len(civils)):
        if find_parent(parent, civils[i - 1][0] * n + civils[i - 1][1]) != find_parent(parent, civils[i][0] * n + civils[i][1]):
            return False
    return True

# bfs
def bfs(civil, visited, parent):
    # 초기 문명이 모두 합쳐진 예제인지 확인
    if check_sets(civil, parent):
        return 0
    # 큐에 초기 문명 좌표들 삽입
    q = deque(civil)
    years = 0
    while q:
        new_area = []
        for _ in range(len(q)):
            y, x = q.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                    new_area.append([ny, nx])
                    visited[ny][nx] = True
                    q.append([ny, nx])


        for y, x in new_area:
            adjacent_union(y, x, visited, parent)

        years += 1

        if check_sets(civil, parent):
            return years

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
parents = [i for i in range(n * n)]

visited = [[False] * n for _ in range(n)]
first_civil = []

for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    visited[a][b] = True
    for i in range(4):
        na, nb = a + dy[i], b + dx[i]
        if 0 <= na < n and 0 <= nb < n and visited[na][nb]:
            union(parents, na*n + nb, a * n + b)
    first_civil.append([a, b])
print(bfs(first_civil, visited, parents))