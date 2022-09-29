'''
세그먼트 트리

'''


# 포화이진트리 배열을 구하는 함수
def getCBT():
    # 포화이진트리의 높이 H
    H = 0
    # 포화 이진트리의 리프노드 개수
    leaf_num = 1
    while leaf_num < n:
        leaf_num *= 2
        H += 1
    # 포화 이진트리의 노드 수는 2 ^ (H + 1) - 1
    return [-1] * (1 << (H + 1))


# 세그먼트 트리 만드는 함수
def init(start, end, idx, segment, array):
    # start == end 가 되면 leaf 노드임
    if start == end:
        segment[idx] = array[start]
        return segment[idx]
    mid = (start + end) // 2
    segment[idx] = init(start, mid, 2 * idx, segment, array) + init(mid + 1, end, 2 * idx + 1, segment, array)
    return segment[idx]


# 세그먼트 트리 갱신 함수 -> 차이로 하는 함수는 백준에 있음
def update(val, k, start, end, segment, array, idx):
    # k가 범위안에 없는 노드라면
    if k < start or k > end:
        return segment[idx]
    # 변경하고자하는 리프노드를 만났을 경우
    if start == end:
        segment[idx] = val
        return val
    mid = (start + end) // 2
    segment[idx] = update(val, k, start, mid, segment, array, idx * 2) + update(val, k, mid + 1, end, segment, array,
                                                                                idx * 2 + 1)
    return segment[idx]


# 구간합 구하기
def findIntervalSum(start, end, left, right, array, segment, idx):
    # 경우의 수 1 : 해당 노드 범위에 완전히 벗어나는 경우
    if end < left or right < start:
        return 0

    # 경우의 수 2: 구하고자 하는 범위에 해당 노드의 범위가 완전히 포함되는 경우
    elif left <= start and end <= right:
        return segment[idx]
    # 경우의 수 3, 4: 해당 노드 범위에 구하고자 하는 범위가 완전히 포함 또는 부분 포함
    else:
        mid = (start + end) // 2
        return findIntervalSum(start, mid, left, right, array, segment, idx * 2) \
               + findIntervalSum(mid + 1, end, left, right, array, segment, idx * 2 + 1)


def main_func():
    segment = getCBT()
    init(0, len(arr) - 1, 1, segment, arr)
    for a, b, c in Query:
        if a == 1:
            arr[b - 1] = c
            update(c, b - 1, 0, len(arr) - 1, segment, arr, 1)
        else:
            print(findIntervalSum(0, len(arr) - 1, b - 1, c - 1, arr, segment, 1))


# 입력 밑 출력 처리
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = []
Query = []
for _ in range(n):
    arr.append(int(input()))

for _ in range(m + k):
    Query.append(list(map(int, input().split())))

main_func()
