import heapq

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def is_valid(y, x):
    return 0 <= y < h and 0 <= x < w and not (table[y][x] == "*")


def dijkstra(start, end):
    pq = []
    for i in range(4):
        distance[i][start[0]][start[1]] = 0
        ny = start[0] + dy[i]
        nx = start[0] + dx[i]
        if (is_valid(ny, nx)):
            heapq.heappush(pq, (0, ny, nx, i))
            distance[i][ny][nx] = 0

    while pq:
        num, y, x, dir = heapq.heappop(pq)
        if num > distance[dir][y][x]: continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            plus = 0
            if not is_valid(ny, nx): continue
            if dir == (i + 2) % 4: continue
            if dir != i: plus += 1

            if distance[i][ny][nx] > num + plus:
                distance[i][ny][nx] = num + plus
                heapq.heappush(pq, (num + plus, ny, nx, i))

    return min(
        distance[0][end[0]][end[1]],
        distance[1][end[0]][end[1]],
        distance[2][end[0]][end[1]],
        distance[3][end[0]][end[1]],
               )

w, h = map(int, input().split())
table = []
distance = [[[float('inf')] * w for _ in range(h)] for _ in range(4)]
lazer = []
for i in range(h):
    a = list(input())
    for j in range(w):
        if a[j] == "C":
            lazer.append((i, j))
    table.append(a)

print(dijkstra(lazer[0], lazer[1]))
