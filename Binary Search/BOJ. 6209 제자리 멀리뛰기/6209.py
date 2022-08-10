'''
제자리 멀리뛰기
돌섬에서 탈출구까지 N개의 작은 돌섬이 있다, 돌섬에서 탈출구까지의 거리는 D이다
N개의 작은 돌섬 중 M개의 돌섬을 제거한 후 탈출구까지 가야 한다.
작은 돌섬을 하나씩 제자리 멀리뛰기로 건넌다.
학생들이 점프하는 최소거리의 최대값을 구하시오

1 <= D <= 1_000_000_000
0 <= N <= 50,000
0 <= M <= N

파라메트릭 서치 문제.
최적화: 학생들이 점프하는 최소 거리의 최대값을 구하시오
결정 : m개의 돌섬을 제거하여 임의의 최소거리 X이상으로 맞출 수 있는가?
있다면 늘려
없다면 줄여

결정함수 -> O(NlogN) 안에 해결해야한다.
주의 : 시작점(0) 과 끝점 (D) 도 포함 해야함.
'''


# 그리디활용한 결정함수
def is_possible(arr, x, m):
    start, end = 0, 0
    count = 0
    while start < len(arr):
        while arr[end] - arr[start] < x:
            end += 1
            if end >= len(arr):
                break
            # 현재 탐색하고 있는 두 수 간의 거리가 X보다 짧다면 count 증가 >> 그리디
            if arr[end] - arr[start] < x:
                count += 1
        start = end
    # 두 수간의 거리가 X보다 짧은 횟수가 주어진 m보다 작거나 같다면 가능한 것!
    return count <= m


def parametric_search(array):
    start, end = 1, int(1e9)
    while start <= end:
        mid = (start + end) // 2

        if is_possible(array, mid, m):
            start = mid + 1
        else:
            end = mid - 1

    return (start + end) // 2



d, n, m = map(int, input().split())
array = [0, d]
for _ in range(n):
    array.append(int(input()))

# print(is_possible(sorted(array), 1, m))
print(parametric_search(sorted(array)))