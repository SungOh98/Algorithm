'''
주사위 윳놀이

시작칸에 4개의 말이 있다.


말 이동 규칙
1. 말이 파란색 칸에서 이동을 시작하면!! 파란색 화살표를 탄다.
2. 이동하는 도중이거나 파란색이 아닌 칸에서 이동을하면 빨간색 화살표를 타야한다.
3. 말이 도착칸에 도달하기만 하면 끝


게임 규칙
1. 게임은 10개의 턴으로 구성
2. 매 턴마다 1~5까지 적힌 주사위를 굴려 도착 칸에 도달하지 않은 말 중 하나를 나온 주사위 수 만큼 이동시킨다.
3. 말이 이동을 마치는 칸에 다른 말이 있다면 그 말은 고를 수 없다.
    단 이동을 마치는 칸이 도착칸이라면 그 도착칸의 말은 고를 수 있다.
4. 말이 이동을 마칠때마다 칸에 적혀 있는 수가 점수에 추가된다.


각 칸에서 다음 칸으로 이동하는 방향은 한가지로 정해져 있다 >> 파란색 화살표 또는 빨간색 화살표

의문 '말이 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다' 에서 그 말이 이동을 마친 말인가, 자리에 있던 말인가?
자리에 있던 말로 하자.


게임의 흐름
1. 4개의 말 중 고를 수 있는 말 중 하나를 고른다. >> 도착칸 말 제외, 전 말이 도착한 곳에 있는 말 제외
2. 주사위의 내용을 보고 이동할 길이를 결정한다.
3. 다음 주사위 길이 만큼 다음 과정을 반복한다.
    1) 진행 방향을 정한다 >> 빨간색 또는 파란색 화살표
    2) 한칸을 이동한다.
4. 도착 후 점수를 계산 한다.


백트래킹은 매 턴마다 어떤 말을 이동시킬지 고르는 여러가지 경우의수를 따질 때 적용한다.
윷놀이 테이블은 static 한 map이므로 구현을 어떻게 할까

그래프 표현을 해야 적당할까?
이차원 테이블로 표현해야 적당할까?
 1   2   3   4    5
[[[있는 말 정보], 점수 정보, 시작 경로, 중간 경로], [], [], [], []]
재귀시 넘겨 줘야할 정보
'''

# 말의 현재 위치와 움직일 거리를 매개값으로 받아
# 이동한 다음 위치를 리턴해주는 함수.
def move(board, loc, length):
    # 초기 출발 위치로 먼저 이동

    loc = board[loc][1]
    length -= 1

    while length > 0:
        loc = board[loc][2]
        length -= 1

    return loc

def backtracking(board, depth, dice, pieces, score, candidate):
    global answer
    # 10번째 턴일 경우 점수 최적화 후 종료
    if depth >= 10:
        answer = max(score, answer)
        return

    # if pieces[0] == pieces[1] == pieces[2] == pieces[3] == 32:
    #     return

    # 현재 턴의 움직일 거리
    length = dice[depth]

    # 다음 고를 수 있는 말 중 하나 고르기.
    for j in range(len(candidate)):
        piece = candidate[j]

        cnt_loc = pieces[piece]

        n_loc = move(board, cnt_loc, length)

        pieces[piece] = n_loc

        # 다음 선택할 수 있는 말의 리스트 뽑기 >> 도착 칸은 제외하고 넘기자!
        cand = []

        flag = True
        # 다음 말을 선택할 후보 리스트
        for i in range(4):
            # 도착하지 않았았다면 삽입.
            if pieces[i] != 32:
                # 현재 말을 제외한 다른 말이 이미 있다면
                if pieces[i] == n_loc and piece != i:
                    flag = False

                cand.append(i)

        if not flag and piece in cand:
            cand.remove(piece)

        score += board[n_loc][0]
        backtracking(board, depth + 1, dice, pieces, score, cand[:])
        score -= board[n_loc][0]

        pieces[piece] = cnt_loc


board = [
    # 0123
    [0, 1, 1], [2, 2, 2], [4, 3, 3], [6, 4, 4],
    # 4567
    [8, 5, 5], [10, 20, 6], [12, 7, 7], [14, 8, 8],
    # 8910 11
    [16, 9, 9], [18, 10, 10], [20, 23, 11], [22, 12, 12],
    # 12 13 14 15
    [24, 13, 13], [26, 14, 14], [28, 15, 15], [30, 27, 16],
    # 16 17 18 19
    [32, 17, 17], [34, 18, 18], [36, 19, 19], [38, 31, 31],
    # 20 21 22 23
    [13, 21, 21], [16, 22, 22], [19, 28, 28], [22, 24, 24],
    # 24 25 26 27
    [24, 28, 28], [26, 28, 28], [27, 25, 25], [28, 26, 26],
    # 28 29 30 31
    [25, 29, 29], [30, 30, 30], [35, 31, 31], [40, 32, 32],
    # 32
    [0, 32, 32]
]

answer = 0
pieces = {}
for i in range(4):
    pieces[i] = 0

dice = list(map(int, input().split()))
# print(move(board, 4, 3))
backtracking(board, 0, dice, pieces, 0, [i for i in range(4)])
print(answer)

















