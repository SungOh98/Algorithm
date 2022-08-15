'''
1 <= N <= 2000 개의 수열이 주어짐
1 <= M <= 1000000 개의 질문이 주어짐
각 질문에 대해 팰린드롬을 만족하면 1, 만족하지 않으면 0을 출력한다.

DP
>> 부분문제의 해답을 이용하여 최종적인 답을 도출하는 최적 부분 구조를 띄어야함.
>> 재귀적 관계식을 도출!
>> bottom up!

1. 관찰을 통해 최적 부분 구조 찾기
2. 용어 정의하기
3. 재귀적 관계식 도출하기
4. 구현하기

용어 정의: p[s:e] : s번째부터 e번째까지 팰린드롬을 만족하나 안하나
최적 부분 구조
p[s:e] 는 p[s + 1:e - 1]의 해답을 활용하여 답을 도출한다.
재귀적 관계식
p[s:e] = p[s + 1 : e - 1] && arr[s] == arr[e]

<bottom up>
(1, 1) (2, 2) (3, 3) (4, 4) (5, 5) (6, 6) (7, 7) >>> 초기값 모두 1임 p[1: 1]은 팰린드롬을 만족하기 때문이다.
(1, 2) (2, 3) (3, 4) (4, 5) (5, 6) (6, 7) >> p[1: 2]까지는 직접 구한다. arr[1] == arr[2] 여부를 조사
(1, 3) (2, 4) (3, 5) (4, 6) (5, 7) >> 여기부터 재귀적 관계식을 활용 ! >> p[1:3] >> p[2:2] && arr[1] == arr[3] 을 통해 도출
...
(1, 7)


'''

def print_board(board):
    for i in board:
        print(i)
def memoization(n, array):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # 초기값 설정
    # p[i:i]
    for i in range(1, n + 1):
        dp[i][i] = 1
    # p[s:e] >> e - s = 1
    for i in range(1, n):
        if array[i] == array[i + 1]:
            dp[i][i + 1] = 1
    width = 2

    while width < n:
        for i in range(1, n - width + 1):
            s, e = i, i + width

            if dp[s + 1][e - 1] and array[s] == array[e]:
                dp[s][e] = 1
        width += 1
    # print_board(dp)

    return dp

import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))
# O(N^2)
dp = memoization(n, array)
m = int(input())
# O(M)
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])
