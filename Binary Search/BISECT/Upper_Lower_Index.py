def Upper_index(arr, start, end, target):
    while start < end: # 상한 / 하한 구현시는 등호 안 붙임!

        mid = (start + end) // 2

        if target >= arr[mid]:
            start = mid + 1

        else:
            end = mid # 상한 / 하한 구현시 mid - 1 안 함!

    return (start + end) // 2


def Lower_index(arr, start, end, target):
    while start < end:

        mid = (start + end) // 2

        if target > arr[mid]:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2


import random

n = int(input())
array = sorted([random.randint(0, n) for _ in range(n)])
print(array)
target = int(input())
print(Upper_index(array, 0, len(array), target))
print(Lower_index(array, 0, len(array), target))
