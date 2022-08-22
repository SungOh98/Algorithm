'''
최대한의 휴식
2 <= N <= 2 x 10^5 일 동안 할당된 일의 양이 주어짐
Amel 이 해야할 총 일의 양 M이 주어짐.
Amel 이 출근한 날들 사이에 일하지 않고 연속해서 쉴 수 있는 연휴들의 최소값의 최대값을 구하자.

1. Parametric Search로 임의의 연휴 x를 정한다.
2. 한번에 쉴 수 있는 최대의 일 수 X로 모든 작업을 처리할 수 있는가? >> 한번에 쉴수 있는 일의 수가 X 이상이여야함.
있다면 >> 늘리기
없다면 >> 줄이기.

결정함수 >> DP
Dp[0][i]는 i일에 일을 하였을 경우 i일까지의 최대 작업량을 기록
Dp[1][i]은 i일에 일을 하지 않았을 경우 i일까지의 최대 작업량을 기록

점화식
Dp[0][i] = max(Dp[0][i - x - 1], Dp[1][i - x - 1]) + Dp[0][i]
Dp[1][i] = max(Dp[0][i - 1], Dp[1][i - 1)

>> max(Dp[0][N], Dp[1][N]) >= M 이라면 최소 휴일 x 로 모든 작업을 처리할 수 있다는 것!

'''
import sys


def is_possible(arr, x, n, task):
    dp = [arr[:]]
    dp.append([0] * (n + 1))
    for i in range(1, n + 1):
        if i - x - 1 >= 0:
            dp[0][i] = max(dp[0][i - x - 1], dp[1][i - x - 1]) + dp[0][i]

        dp[1][i] = max(dp[0][i - 1], dp[1][i - 1])
    return max(dp[0][n], dp[1][n]) >= task


def parametric_search(arr, task, n):
    start, end = 0, 2 * int(1e5)

    while start <= end:
        mid = (start + end) // 2
        if is_possible(arr, mid, n, task):
            start = mid + 1

        else:
            end = mid - 1
    return (start + end) // 2

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = [0] + list(map(int, input().split()))
# print(is_possible(array, 4, n, m))
answer = parametric_search(array, m, n)

print(answer if answer != 2 * int(1e5) else "Free!")