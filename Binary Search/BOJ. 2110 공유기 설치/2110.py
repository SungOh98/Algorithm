'''
나무 자르기 BOJ 2805 과 비슷한 파라메트릭 서치 문제.
1. 최적화 문제를 결정문제로 변환 가능한지 여부를 확인한다.
최적화문제:  집들 사이의 공유기간의 최대 거리 x >> 결정 문제: 거리가 x 일때 공유기 C개를 설치할 수 있는가??
2. 공유기간의 거리 x가 증가 / 감소함수로 표현할 수 있는가? >> okay

알고리즘
거리 x를 0 ~ 1e9까지 이분 탐색으로 설정해가며 설치 가능여부를 따진다.
설치가 가능할 경우 > 거리 탐색 범위를 mid + 1 ~ end 로 조정하여 다음 mid 값을 늘린다.
설치가 불가할 경우 > 거리 탐색 범위를 start ~ mid - 1로 조정하여 다음 mid 값을 줄인다.
>> 하나의 값으로 수렴할 때 까지 이분탐색을 진행한다.
>> mid 값이 공유기간의 거리 X가 된다.

'''

def is_Possible(arr, c, dist):
    start, end = 0, 0
    c -= 1

    while c > 0:

        while end < len(arr) and (arr[end] - arr[start] < dist):
            end += 1

        if end >= len(arr):
            break

        start = end
        c -= 1

    return c <= 0

def parametric_search(array, c):
    start, end = 0, max(array)
    # start, end = 0, 1_000_000_000
    # mid가 거리 x임
    # 하나의 x로 수렴할 때까지 이진 탐색을 수행!
    while start <= end:
        mid = (start + end) // 2

        # 거리 x가 설치 가능하다면 >> 거리를 늘리자
        if is_Possible(array, c, mid):
            start = mid + 1
        # 거리 X가 설치 불가능하다면 >> 거리를 줄이자
        else:
            end = mid - 1

    return (start + end) // 2


# print(is_Possible([1, 2, 4, 8, 9], 3, 3))
n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()
print(parametric_search(array, c))