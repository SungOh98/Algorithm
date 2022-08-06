'''
구간 나누기 2
크기가 N인 배열을
M개이하의 부분 배열로 나누려고 한다
각 부분 배열은 크기가 N인 배열에서 위치가 연속된 수들로 이루어진다. 크기는 1이상
구간의 점수는 각 부분 배열의 최대값 - 최소값으로 정의하고
구간의 점수들의 최대값의 최소값을 구하려고 한다.

1 <= N, M <= 5000
>>O( N^2 log K) 의 알고리즘 설계가 필요하다. K는 임의의 수

1. 파라메트릭 서치로 임의의 최소값 X를 구한다.
2. N^2 으로 최소값 X로 구간을 나눌 수 있는지 여부를 판단한다.
>> 나눌 수 없다면 최소값 X를 늘린다.
>> 나눌 수 있다면 최소값 X를 줄인다.


'''

def is_possible(arr, x, m):
    # 투 포인터를 활용해 확인
    start, end = 0, 0

    while start < len(arr):
        min_v, max_v = arr[start], arr[start]
        m -= 1
        while max_v - min_v <= x:
            end += 1
            if end >= len(arr):
                break
            max_v = max(max_v, arr[end])
            min_v = min(min_v, arr[end])

        start = end

    # m개 이하로 가능했는지?
    return m >= 0

def parametric_search(arr, m):
    start, end = 0, 10000

    while start < end:
        mid = (start + end) // 2

        if is_possible(arr, mid, m):
            end = mid

        else:
            start = mid + 1

    return (start + end) // 2

n, m = map(int, input().split())
array = list(map(int, input().split()))
print(parametric_search(array, m))
# x = int(input())
# print(is_possible(array, x, m))

