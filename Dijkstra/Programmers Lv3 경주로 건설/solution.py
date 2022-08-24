'''
2차원 격자
1은 벽 0은 빈칸
출발 : 0, 0
도착: n-1, n-1
경주로는 상하좌우 인접한 칸에 연결할 수 있다.
벽이 있다면 연결 불가
직선 도로 : 100 원
코너 : 500원

뭔가 다익스트라 같다.
cost[i][j] 를 0, 0 부터 출발하여 i, j 까지 도달하는데 드는 최소 비용
반례
8
00000000
10111110
10010000
11000111
11110000
11111110
11111110
11111110
ans: 4500
'''
import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def cal_cost(p_d, d):
    if d == p_d:
        return 100
    else:
        return 600


def next_dir(d):
    if d == 0:
        return (0, 2, 3)
    elif d == 1:
        return (1, 2, 3)
    elif d == 2:
        return (0, 1, 2)
    else:
        return (0, 1, 3)


def dijkstra(n, board):
    costs = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    for i in range(4):
        costs[0][0][i] = 0
    pq = []
    if board[1][0] != 1:
        costs[1][0][1] = 100
        heapq.heappush(pq, (100, 1, 0, 1))
    if board[0][1] != 1:
        costs[0][1][3] = 100
        heapq.heappush(pq, (100, 0, 1, 3))

    while pq:
        cost, y, x, d = heapq.heappop(pq)
        if cost > costs[y][x][d]:
            continue
        for i in next_dir(d):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if board[ny][nx] != 1:

                    if costs[ny][nx][i] > cost + cal_cost(d, i):
                        costs[ny][nx][i] = cost + cal_cost(d, i)
                        heapq.heappush(pq, (costs[ny][nx][i], ny, nx, i))
    return min(costs[n - 1][n - 1])


def solution(board):
    answer = dijkstra(len(board), board)
    return answer
# board = []
# n = int(input())
# for _ in range(n):
#     board.append(list(map(int, input())))
# print(board)
# print(solution(board))

