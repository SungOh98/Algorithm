'''
원장 선생님 깨서는 1~ n까지의 학생들 중에서 k명의 학생들을 소풍에 보내려고 한다.
k명이 모두 친구사이 이길 원한다.
친구관계의 정보가 주어질 때 소풍가게될 K명을 결정하시오
출력은 오름차순으로 학생을 출력하되, 여러 팀이 나올 경우 팀 들 중 첫번째 학생이 가장 작은 팀을 출력하시오
첫번째 학생이 같다면 두번째학생을 기준으로 ,,, 이런식으로 출력하시오

이 문제는 최적화문제가 아니라 결정문제이다.
따라서 모든 상태공간 트리를 탐색하지 말고 정답을 만나면 바로 종료를 해야한다.

무조건 시간초과 뜰 것 같은데 일단해보자.

1. 인접행렬으로 친구관계 그래프 생성.
2. 백트래킹 >> is_Vaild() 함수를 통해 유효한 경우만 가지를 뻗어나가기.
3. 정답을 만난다면 리턴!
'''

def print_board(board):
    for i in board:
        print(i)
    print()

def is_Vaild(friend, current, number):
    for num in current:
        if not friend[num][number]:
            return False

    return True

def combination(idx, depth, ans, friend):
    global terminate
    if terminate:
        return

    if depth == k:
        terminate =True
        for i in ans:
            print(i)
        return

    for i in range(idx, n + 1):
        if is_Vaild(friend, ans, i):
            combination(i + 1, depth + 1, ans + [i], friend)
import sys
input = sys.stdin.readline
k, n, f = map(int, input().split())
adjacent_matrix = [[False] * (n + 1) for _ in range(n + 1)]
terminate = False
for _ in range(f):
    a, b = map(int, input().split())
    adjacent_matrix[a][b] = True
    adjacent_matrix[b][a] = True

for i in range(1, n):
    adjacent_matrix[i][i] = True

# print_board(adjacent_matrix)
combination(1, 0, [], adjacent_matrix)
if not terminate:
    print(-1)