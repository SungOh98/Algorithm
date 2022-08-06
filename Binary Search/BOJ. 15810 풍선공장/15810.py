'''
풍선 공장
n명의 스태프가 있고 , 각 스태프마다 풍선을 만드는데 걸리는 시간이 다르다.
풍선 M개를 만드는데 걸리는 최소시간을 구하여라.

1 <= N, M < 1,000,000
> 입력의 크기가 크기때문에 이분탐색 의심

최적화 문제: M개의 풍선을 만드는데 걸리는 최소시간?
결정문제 : 임의의 시간 X 동안 M개의 풍선을 만들 수 있는가?
>> 있다면 시간 줄임
>> 없다면 시간 늘림
'''


def is_possible(arr, x, m):
    for i in arr:
        m -= x // i
    return m <= 0


def parametric_search(arr, m):
    start, end = 1, int(1e12)

    while start < end:
        mid = (start + end) // 2

        if is_possible(arr, mid, m):
            end = mid

        else:
            start = mid + 1

    return (start + end) // 2
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = list(map(int, input().split()))
print(parametric_search(array, m))
