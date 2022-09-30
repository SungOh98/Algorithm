import math
import sys

'''
12
5 8 7 3 2 5 1 8 9 8 7 3
3
2 2 5
1 2 1
2 1 4
'''


def init(start, end, idx, arr, segment):
    if start == end:
        segment[idx] = arr[start]
        return segment[idx]

    mid = (start + end) // 2
    segment[idx] = min(init(start, mid, idx * 2, arr, segment), init(mid + 1, end, idx * 2 + 1, arr, segment))
    return segment[idx]


def intervalMin(start, end, segment, idx, left, right):
    # 범위 벗어난 경우
    if right < start or end < left:
        return float('inf')

    elif left <= start and end <= right:
        return segment[idx]

    else:
        mid = (start + end) // 2
        tmp = min(intervalMin(start, mid, segment, 2 * idx, left, right),
                  intervalMin(mid + 1, end, segment, 2 * idx + 1, left, right))
        return tmp


def update(val, k, start, end, idx, segment):
    # 범위를 벗어난 경우
    if k < start or k > end:
        return segment[idx]
    if start == end:
        segment[idx] = val
        return val
    mid = (start + end) // 2
    segment[idx] = min(update(val, k, start, mid, 2 * idx, segment), update(val, k, mid + 1, end, 2 * idx + 1, segment))
    return segment[idx]


input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
Query = []
H = math.ceil(math.log2(n))
seg = [-1] * (1 << (H + 1))
init(0, n - 1, 1, arr, seg)

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    Query.append((a, b, c))
for a, b, c in Query:
    if a == 1:
        update(c, b - 1, 0, n - 1, 1, seg)
    else:
        print(intervalMin(0, n - 1, seg, 1, b - 1, c - 1))
