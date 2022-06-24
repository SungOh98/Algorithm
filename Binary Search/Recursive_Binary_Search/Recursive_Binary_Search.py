import random

'''
이진 탐색은 정렬되어 있는 배열에서만 활용가능하다.
time complexity = O(logN)
'''


def Binary_search(arr, start, end, target):
    mid = (start + end) // 2
    if start > end:
        return "해당 값이 배열에 존재하지 않습니다."

    elif arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return Binary_search(arr, start, mid - 1, target)

    else:
        return Binary_search(arr, mid + 1, end, target)


n = int(input("배열의 크기 입력: "))
arr = []
for _ in range(n):
    arr.append(random.randint(-30, 30))
arr.sort()
print(arr)
t = int(input("찾고자 하는 데이터 입력: "))
print(Binary_search(arr, 0, len(arr) - 1, t))
