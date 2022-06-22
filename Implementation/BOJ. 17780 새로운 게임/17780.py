'''
새로운 게임
체스판 말이용
말의 갯수는 k개
하나의 말 위에 다른 말을 올릴 수 있다. >> 업는 느낌
맨 아래의 말만 이동시킬 수 있다.
턴 한번 : 1번 말~ k번 말까지 차례로 이동

말이 4개 이상 쌓이는 순간 게임이 종료됨


이동 규칙
    1. 이동하려는 칸이 흰색일 경우 그냥 이동
        이동하려는 칸에 말이 이미 있을 경우 맨위에 말이 올라감
    2. 빨간색일 경우 이동 후 이동하기 전에 있던 말들의 위치를 뒤집는다.
    3. 이동하려는 칸이 파란색이거나 격자 바깥이라면 방향을 바꾸고 이동한다.
        방향을 바꾸고 이동하려는 칸도 파란색이라면 이동하지 않고 방향만 바꾼다.



격자안에 색깔 저장해야함.

각 말마다
좌표 저장, 방향 저장.

board >> 3차원 list
color >> 2차원 list
격자안에 표시해두지 않으면 debug하기 어렵기 때문에 테이블을 2개 설정해서 가자.

0 : 흰, 1: 빨, 2: 파
'''

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def dir_change(dir):
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    else:
        return 2


def print_board(board):
    for i in board:
        print(i)
    print()


'''
이동 할 시 자신이 맨 밑의 말 인지 확인함.
이동 후 정보 갱신하는 것 잊지 말기
'''


def horse_move(info, num, board, color):
    y, x, d = info[num]
    # 이동하려는 말이 맨 밑에 있는 말이 아닐 경우 종료
    if board[y][x][0] != num:
        return

    ny, nx = y + dy[d], x + dx[d]

    # 범위 밖이거나 파란색일 경우
    if (ny >= n or ny < 0 or nx >= n or nx < 0) or color[ny][nx] == 2:
        d = dir_change(d)
        # 한번더 살피기
        ny, nx = y + dy[d], x + dx[d]
        # 범위 밖이거나 파란색일 경우
        if (ny >= n or ny < 0 or nx >= n or nx < 0) or color[ny][nx] == 2:
            # 바뀐 방향만 기록하고 종료
            info[num][2] = d
            return
        # 이동할 수 있는 칸일 경우 >> 재귀?
        else:
            info[num][2] = d
            horse_move(info, num, board, color)

    # 범위 안이면서 흰 색일 경우
    elif color[ny][nx] == 0:
        # 이동
        board[ny][nx] += board[y][x]
        board[y][x] = []
        # 정보 갱신
        for i in board[ny][nx]:
            info[i][0], info[i][1] = ny, nx
    # 범위 안이면서 빨간 색일 경우
    else:
        # 이동
        board[ny][nx] += reversed(board[y][x])
        board[y][x] = []
        # 정보 갱신
        for i in board[ny][nx]:
            info[i][0], info[i][1] = ny, nx


def terminate(board, info):
    for num in info:
        y, x, d = info[num]
        if len(board[y][x]) >= 4:
            return True
    return False


def main_func(board, info, color):
    turn = 0
    while not terminate(board, info) and turn <= 1000:
        for i in range(1, m + 1):
            horse_move(info, i, board, color)
        turn += 1
    if turn > 1000:
        return -1
    else:
        return turn


n, m = map(int, input().split())
info = {}

color = [list(map(int, input().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for _ in range(n)]

# for i in board:
#     print(i)
for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    info[i] = [a - 1, b - 1, c - 1]
    board[a - 1][b - 1].append(i)

print(main_func(board, info, color))
# print_board(board)
# horse_move(info, 1, board, color)
# print_board(board)
