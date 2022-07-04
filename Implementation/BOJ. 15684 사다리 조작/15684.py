'''
사다리 조작

세로선들 사이에 가로선을 설치하는데

두 가로선이 연속하거나, 서로 접하면 안된다., 또 가로선은 점선 위에 있얼야한다.

사다리 게임은 각각의 세로선마다 게임을 진행하고 세로선의 가장 위에서 부터 시작해야한다.

사다리에 가로선을 추가해서 사다리 게임의 결과를 조작하려한다. i번 세로선에서 출발하면 i번 세로선에 도착해야함.
추가해야하는 가로선의 최솟값을 출력하시오

전략
모든 좌표들에 대해 사다리 세개를 놓은 경우를 모두 따짐.


시뮬레이션 함수로 돌려봐
진짜 이상한 실수를 했네
조합으로 생각하고 순열로 짜버렸네
'''

# 상: 0 하: 1 좌:2  우:3
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isvaild(y, x, board):
    if board[y][x] == 1 and board[y][x + 1] == 1:
        return True
    else:
        return False

def abstract_coordinate(board):
    tmp = []
    for i in range(h):
        for j in range(n - 1):
            if board[i][j] == 1 and board[i][j + 1] == 1:
                tmp.append((i, j))
    return tmp

def print_board(board):
    for i in board:
        print(i)

def find_next_width(y, x, board):
    dire = board[y][x]

    ny, nx = y + dy[dire], x + dx[dire]

    if dire == 1:
        return [ny, nx]

    return [ny + dy[1], nx + dx[1]]

'''결과가 맞는지 확인해보는 함수'''
def simulation(board):
    for x in range(n):
        ny, nx = 0, x

        while ny < h:
            ny, nx = find_next_width(ny, nx, board)

        if nx != x:
            return False

    return True

def backtracking(coordinate, depth, idx, board):
    global ans

    if depth <= 3:

        if depth == 3:

            if simulation(board):
                ans = min(ans, depth)
            return

        if simulation(board):
            ans = min(ans, depth)


        for i in range(idx, len(coordinate)):
            y, x = coordinate[i]

            # 유효하지 않을 경우 >> 사다리가 연속으로 놓일 경우
            if not isvaild(y, x, board):
                continue

            # tmp = [k[:] for k in board]

            board[y][x] = 3
            board[y][x + 1] = 2

            backtracking(coordinate, depth + 1, i + 1, board)
            # board = tmp
            board[y][x], board[y][x + 1] = 1, 1





n, m, h = map(int, input().split())
board = [[1] * n for _ in range(h)]

width = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    board[a][b], board[a][b + 1] = 3, 2

ans = float('inf')
# print(find_next_width(0, 2, board))
# simulation(board)
coordinate = abstract_coordinate(board)
# print(coordinate)
# print_board(board)
backtracking(coordinate,  0, 0, board)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
# print(coordinate)
# board[4][3], board[4][4], board[5][1], board[5][2] = 3, 2, 3, 2
# print(simulation(board))