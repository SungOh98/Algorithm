def bisect_left(start, end, target, arr):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2


def bisect_right(start, end, target, arr):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] <= target:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2

import sys
input = sys.stdin.readline
n = int(input())
arr1, arr2, arr3, arr4 = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr1.append(a)
    arr2.append(b)
    arr3.append(c)
    arr4.append(d)
array1, array2 = [], []

# n^2 : 배열 4개를 2개의 배열로 축소 ! >> 2개의 배열의 각 요소를 더한 경우의 수를 나열하는 새로운 배열!
for i in range(n):
    for j in range(n):
        array1.append(arr1[i] + arr2[j])
        array2.append(arr3[i] + arr4[j])
array1.sort()
array2.sort()
# print(array1)
# print(array2)
answer = 0
# n^2 * (log n^2)
for i in range(len(array1)):
    answer += (bisect_right(0, len(array2) - 1, -array1[i], array2) - bisect_left(0, len(array2) - 1, - array1[i],
                                                                                  array2))
print(answer)
