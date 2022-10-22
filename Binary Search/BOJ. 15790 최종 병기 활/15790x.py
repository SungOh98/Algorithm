'''
N 길이의 둘레를 기진 고무줄
북 방향에서 시계방향으로 1 증가함.
고무줄 M개에 홈이 파여있음.
홈이 파인 위치: 0 ~ N-1 사이의 정수
홈이 파인 곳만 고무줄을 절단할 수 있음
주어진 고무줄을 절단하여 K 겹의 직선 고무줄을 만들려고 함.
활의 길이는 절단하여 생긴 K개의 고무줄 중 가장 길이가 짧은 고무줄로 결정됨.
만들 수 있는 가장 긴 활의 길이는?

1 <= N <= 100000
1 <= M <= min(N, 1000)
1 <= K <= M


1. 최적화 -> 결정
만들 수 있는 활의 길이의 Max 값 -> 활의 길이가 X일 때 K겹의 고무줄을 만들 수 있는가?
만들 수 있다면 -> 늘리기
만들 수 없다면 -> 줄이기

1개만 파였다면 >> 고무줄 하나만 만들 수 있음.
K개의 고무줄 보다 많이 나온다면 나머지는 버려도 됨.

'''



# 배열에 N + arr[0] 를 추가해주면 가능할 것 같다.

def is_possible(arr, k, x):
    start, end = 0, 0
    cnt = 0
    while end < len(arr):
        while end < len(arr) and arr[end] - arr[start] < x:
            end += 1

        if end >= len(arr):
            break
        cnt += 1
        start = end
    return cnt >= k


def parametric_search():
    start, end = 1, 100_000

    while start <= end:
        mid = (start + end) // 2

        if is_possible(arr, k, mid):
            start = mid + 1
        else:
            end = mid - 1

    answer = (start + end) // 2

    return answer if answer != 0 else -1


import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(int(input()))
arr.append(n + arr[0])

print(parametric_search())
