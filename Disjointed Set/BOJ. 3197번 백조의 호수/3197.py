# 백조의 호수 재도전
'''
<내 핵심 아이디어>
disjointed set 을 활용한 breadth first search
disjointed set은 각 물의 영역(집합)의 대표노드를 명시하기 위해 사용
>> 백조1의 대표노드와 백조2의 대표노드가 같아지면 백조 두마리가 만날 수 있게 된다는 의미

<내 procedure>
1. bfs를 통해 초기 물의 영역에 대한 make set, 추가로 물의 영역의 가장자리에 있는 얼음들의 좌표를 기록
2. 백조1과 백조2가 같은 집합이 될때까지 다음과정을 수행
    - 1에서 구한 얼음들을 녹인다.
        - 각 녹이는 얼음들의 인접한 구역이 물이나 백조일 경우 > 녹인 영역을 인접구역과 union
        - 각 녹이는 얼음들의 인접한 구역이 얼음일 경우 > 다음에 녹일 얼음 좌표들에 기록
3. 날짜 도출

각 노드의 parent는 다음과 같이 구현
[1, 2, 3
4, 5, 6
7, 8, 9]
'''


# disjointed set
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


# 물일 경우만 서치
def Breadth_First_Search(parent, board, visited, y, x):
    visited[y][x] = True
    q = deque()
    q.append((y, x))
    melt_cand = set()
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 범위 안이면서 방문하지 않은 곳 탐색
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                # 물이라면
                if board[ny][nx] == "." or board[ny][nx] == "L":
                    # 같은 집합으로 묶어
                    union(parent, parent[y * m + x], parent[ny * m + nx])
                    # 방문처리
                    visited[ny][nx] = True
                    # 큐에 삽입
                    q.append((ny, nx))
                    # 녹일 후보에 추가.

                # 빙판이라면
                else:
                    melt_cand.add((ny, nx))

    return melt_cand


def melting_ice(candidate, parent):
    next_cand = set()
    for y, x in candidate:
        # 얼음 녹이고
        board[y][x] = "."

        # 인접 구역봐서 다음 녹일 좌표들 얻기
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                # 인접 좌표가 얼음이라면 다음 후보에 저장
                if board[ny][nx] == "X":
                    next_cand.add((ny, nx))
                # 백조이거나 물이라면 >> Union
                else:
                    if find_parent(parent, y * m + x) != find_parent(parent, ny * m + nx):
                        union(parent, y * m + x, ny * m + nx)

    return next_cand



def main_func():
    visited = [[False] * m for _ in range(n)]
    melt_candidate = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] != "X" and not visited[i][j]:
                melt_candidate |= Breadth_First_Search(parents, board, visited, i, j)

    days = 0
    swan_1, swan_2 = swans[0], swans[1]
    while find_parent(parents, swan_1[0] * m + swan_1[1]) != find_parent(parents, swan_2[0] * m + swan_2[1]):
        melt_candidate = melting_ice(melt_candidate, parents)
        days += 1
    return days


from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, (input().split()))
board = []
swans = []
parents = [i for i in range(n * m)]
for i in range(n):
    a = list(input())
    for j in range(m):
        if a[j] == "L":
            swans.append((i, j))
    board.append(a)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
print(main_func())