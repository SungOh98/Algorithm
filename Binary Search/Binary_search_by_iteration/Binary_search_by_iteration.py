import random

'''
이진 탐색은 정렬되어 있는 배열에서만 활용가능하다.
time complexity = O(logN)
'''
def binary_search(arr, target):
    start, end = 0, len(arr) - 1

    while start <= end:
        # 중간 값 지정
        mid = (start + end) // 2
        # 원하는 값이 현재 배열의 중간 값과 같다면 그 중간을 리턴
        if target == arr[mid]:
            return mid
        # 원하는 값이 현재 배열의 중간 값보다 크다면 배열의 탐색 범위를 중간 이후로 변경
        elif target > arr[mid]:
            start = mid + 1
        # 원하는 값이 현재 배열의 중간 값보다 작다면 배열의 탐색 범위를 중간 이전으로 변경
        else:
            end = mid - 1
    # while 문이 끝나도록 리턴 값이 없다면 원하는 값이 배열에 없는 것
    return "배열에 해당 값이 존재하지 않습니다."

n = int(input("배열의 크기 입력: "))
arr = []
for _ in range(n):
    arr.append(random.randint(-10, 30))


arr.sort()
print(arr)
t = int(input("찾고자 하는 데이터 입력: "))
print(binary_search(arr, t))


