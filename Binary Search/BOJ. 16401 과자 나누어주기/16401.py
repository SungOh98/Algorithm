'''
조카들을 달래기 위해 홍익이는 막대과자를 하나씩 나누어준다.
조카들이 과자를 먹는동안 떼를 쓰지 않기 때문에 최대한 긴 과자를 나누어 주려고 한다.
그런데 나누어 준 과자의 길이가 다르다면 조카들이 화를 내기 때문에 똑같은 길이의 과자를 나누어 주어야 한다.
m명의 조카가 있고, n개의 과자가 있을 때, 조카 1명에게 줄 수 있는 과자의 최대길이를 구하여라.
단 막대과자는 길이와 상관없이 여러 조각으로 나누질 수 있지만, 과자를 하나로 합칠 수는 없다.

예제
4 3
10 10 15
s : 0 e: 14 mid : 7
s : 8 e: 14 mid : 11
s : 8 e: 10 mid : 9
s : 8 e : 8 mid : 8
s : 8 e : 7 -> break

3 10
1 2 3 4 5 6 7 8 9 10


15 짜리 과자를 7두개로 나누어 총 7길이의 과자 4개를 나누어 줄 수 있다.

최대 최소 문제 + 입력값이 무지막지하게 크다 >> 파라메트릭 서치 의심!

1. 최적화문제를 결정문제로 바꿀 수 있는가?
임의의 과자 길이 x로 m명의 조카에게 과자를 모두 나누어줄 수 있는가?
2. 임의의 과자 길이가 증가 / 감소 함수로 접근 가능한가? >> 증가함수로 접근 가능하다!

5 3
1 2 1
ans : 0
s: 0 e: 3 mid : 1
s : 0 e : 0

1 1,000,000
10억 .... 10억

3
'''

def is_possible(x):
    # 0이면 안나눠줘도 됨 -> 무조건 true.
    if x == 0: return True
    cnt = 0
    for snack in snacks:
        cnt += snack // x
    return cnt >= m

def parametric_search():
    start, end = 0, int(1e9)
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        if is_possible(mid):
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

import sys
input = sys.stdin.readline
m, n = map(int, input().split())
snacks = list(map(int, input().split()))
print(parametric_search())