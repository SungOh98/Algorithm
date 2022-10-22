'''
모노미노도미노2

보드는 빨간색, 파란색, 초록색 보드가 붙어있다.

사용 블록
1 by 1, 1 by 2, 2 by 1

1. 블록을 놓을 취리를 빨간색 보드에서 선택한다.
2. 그 위치부터 초록색 / 파란색 보드로 블록이 이동한다.
    블록의 이동은 다른 블록을 만나거나 보드의 경계를 만날때 까지 이동한다.
3. boom
    초록색 보드의 한 행이 가득 찬다면 그 행은 모두 사라짐
    사라진 이후 사라진 행 위의 타일들이 사라진 행의 수만큼 아래로 이동
    파란색 보드의 한 열이 가득 찬다면 그 열은 모두 사라짐.
    사라진 이후 사라진 열 왼쪽의 타일들이 사라진 열의 수만큼 오른쪽으로 이동

    행이나 열이 사라질 경우 1점 획득

초록색 보드의 0, 1 번 행 과 파란색 보드의 0, 1 번 열 >> 특별한 칸
초록색 보드의 0, 1번 행에 블록이 있다면 맨 아래행부터 1개 또는 2개의 행이 사라진 후 떨어짐

행이나 열이 가득찬 경우와 연한 칸에 블록이 있는 경우가 동시에 발생할 경우
>> 행이나 열이 타일로 가득 찬 경우가 없을 때까지 점수를 획득하는 과정이 모두 진행 된 후
연한 칸에 블록이 있는 경우를 처리함.

블록을 놓은 위치가 순서대로 주어졌을 때 얻은 점수와 초록색 보드와 파란색 보드에 타일이 있는 칸의
개수를 구해보자.
2시 시작

1 <= N <= 10000
t = 1 : 1 by 1
t = 2 : 1 by 2
t = 3 : 2 by 1

1. 블록 두기
2. 블록 이동
3. 블록 계산
4. 블록 열 이동
5. 특별한 칸 처리

파란색은 돌려서 생각하자.

'''
import sys

input = sys.stdin.readline


def outOfBound(coordinate):
    for y, x in coordinate:
        if y >= end:
            return True
    return False


def crash(coordinate, board):
    for y, x in coordinate:
        if board[y][x] == 1:
            return True
    return False


def move(coordinate, board):
    while not outOfBound(coordinate) and not crash(coordinate, board):
        for i in range(len(coordinate)):
            coordinate[i][0] += 1
    for y, x in coordinate:
        board[y - 1][x] = 1


def forBlue(coordinate):
    new = []
    for y, x in coordinate:
        new.append([x, 3 - y])
    return new


def changeInput(type, y, x):
    if type == 1:
        return [[y, x]]
    elif type == 2:
        return [[y, x], [y, x + 1]]
    else:
        return [[y, x], [y + 1, x]]


def print_board(board):
    for i in board:
        print(i)
    print()


def plusScore(board):
    global score
    idxs = []
    for i in range(start, end):
        flag = True
        for j in range(4):
            if board[i][j] == 0:
                flag = False
                break
        if flag:
            idxs.append(i)
    score += len(idxs)
    for idx in idxs:
        for i in range(4):
            board[idx][i] = 0

    if len(idxs) > 0:
        return idxs[0] - 1, len(idxs)
    else:
        return -1, 0


# 모양을 유지하며 떨어지는 것 주의 + 최대 2칸씩만 연속하여 떨어질 수 있음
def drop(board, tmp):
    drop_start, cnt = tmp[0], tmp[1]
    if cnt > 0:
        for i in range(drop_start, -1, -1):
            for j in range(4):
                board[i + cnt][j] = board[i][j]
                board[i][j] = 0


def special(board):
    drop_length = 0
    drop_start = 9
    for i in range(5, 3, -1):
        flag = False
        for j in range(4):
            if board[i][j] == 1:
                flag = True
                break
        if flag:
            drop_length += 1
    for _ in range(drop_length):
        for i in range(4):
            board[drop_start][i] = 0
        drop_start -= 1
    return drop_start, drop_length


def getAnswer(board):
    cnt = 0
    for i in range(start, end):
        for j in range(4):
            if board[i][j] == 1:
                cnt += 1
    return cnt

score = 0

def main_func():
    global score
    N = int(input())
    for _ in range(N):
        t, a, b = map(int, input().split())
        coordinate = changeInput(t, a, b)
        move(forBlue(coordinate), bBoard)
        move(coordinate, gBoard)
        drop(bBoard, plusScore(bBoard))
        drop(gBoard, plusScore(gBoard))
        drop(bBoard, special(bBoard))
        drop(gBoard, special(gBoard))

        # print("---------------------")
        # print_board(bBoard)
        # print_board(gBoard)
    print(score)
    print(getAnswer(bBoard) + getAnswer(gBoard))


start, end = 6, 10

gBoard = [[0] * 4 for _ in range(end)]
bBoard = [[0] * 4 for _ in range(end)]

main_func()
