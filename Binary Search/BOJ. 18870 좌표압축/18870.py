import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
# 중복 제거
arr = sorted(set(array))
# print(array)
# print(arr)
# 범위를 벗어나는 일이 없는 문제임
def binary_search(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(start, mid, arr, target)
    else:
        return binary_search(mid + 1, end, arr, target)

for num in array:
    print(binary_search(0, len(arr) - 1, arr, num), end=" ")