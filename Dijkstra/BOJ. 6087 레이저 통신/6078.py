'''
레이저 통신
다익스트라 활용문제는 dist 배열에 뭘 저장할지를 잘 생각해야한다.
또한 BFS처럼 도착점을 만나면 바로 종료하는게 아니라
모든 알고리즘 동작 후에 목표로하는 노드 i의 dist[i]를 얻는 형식인 것 같다.

table[i][j]를 각 노드로 봄
dist[i][j] 에 table[i][j]에 도달하기 위한 최소 거울 사용 횟수를 저장한다.
다익스트라 돌린 후 다른 C가 있는 노드의 dist[i][j]를 얻는다.

거울을 사용했다는 것을 어떻게 정의하지?
큐에 push할때 방향 벡터 정보를 주어주면 어떨까?

반례
4 5
C..*
...*
...*
*.**
...C

답: 2
'''
import heapq
# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def get_next_dir(dir):
    # 상 방향일 때
    if dir == 0:
        return (0, 2, 3)
    # 하 방향일 때
    elif dir == 1:
        return (1, 2, 3)
    # 좌 방향일 때

    elif dir == 2:
        return (0, 1, 2)

    else:
        return (0, 1, 3)

def dijkstra(start, end, distance, table):
    # 출발 노드의 거울 사용 횟수는 0
    distance[start[0]][start[1]] = 0
    pq = []
    for i in range(4):
        start_y, start_x = start[0] + dy[i], start[1] + dx[i]
        if 0 <= start_y < h and 0 <= start_x < w and table[start_y][start_x] != "*":
            distance[start_y][start_x] = 0
            heapq.heappush(pq, [0, start_y, start_x, i])

    while pq:
        dist, y, x, dir = heapq.heappop(pq)

        # 갱신 안된 정보라면 무시
        if dist > distance[y][x]:
            continue

        # 인접 노드 사용 거울 개수 갱신

        for i in get_next_dir(dir):
            # 인접 노드 좌표
            ny, nx = y + dy[i], x + dx[i]

            # 다음 좌표가 벽이거나 격자 밖이라면 무시
            if (ny >= h or ny < 0 or nx >= w or nx < 0) or table[ny][nx] == "*":
                continue
            # 이전과 같은 방향이라면 거울 개수 추가안함
            if i == dir:
                if distance[ny][nx] >= dist:
                    distance[ny][nx] = dist
                    heapq.heappush(pq, [distance[ny][nx], ny, nx, i])
            # 이전과 다른 방향이라면 거울 개수 추가함
            else:
                # 바로가는 것보다 거쳐가는게 거울 개수를 더 적게 쓴다면
                if distance[ny][nx] >= dist + 1:
                    # 갱신 후
                    distance[ny][nx] = dist + 1
                    # pq에 삽입
                    heapq.heappush(pq, [distance[ny][nx], ny, nx, i])
    return distance[end[0]][end[1]]

w, h = map(int, input().split())
table = []
distance = [[float('inf')] * w for _ in range(h)]
lazer = []
for i in range(h):
    a = list(input())
    for j in range(w):
        if a[j] == "C":
            lazer.append((i, j))
    table.append(a)

print(dijkstra(lazer[0], lazer[1], distance, table))