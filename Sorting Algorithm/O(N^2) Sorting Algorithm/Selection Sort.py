'''
Selection Sort
현재 배열의 탐색 범위에서 최댓값을 찾고 현재 배열의 탐색 범위의 맨 끝의 원소와 자리를 바꾸는 알고리즘.
버블 소트와 마찬가지로 배열의 뒤에서부터 정렬이 완료됨.
단위연산을 비교연산으로 잡는다면 버블 소트와 똑같은 time complexity 가 도출됨.
time complexity = theta(N^2)

'''

def selection_sort(arr, n: "배열의 마지막 인덱스"):
    for swap_idx in range(n, 0, -1):
        max_idx, max_v = 0, arr[0]
        for i in range(1, swap_idx + 1):
            # 단위 연산 >> 비교 문장!
            if arr[i] > max_v:
                max_idx, max_v = i, arr[i]
        # swap
        arr[max_idx], arr[swap_idx] = arr[swap_idx], arr[max_idx]

    return arr

import random

TC = int(input())
n = 20
# n = int(input("배열의 크기를 입력하세요: "))
flag = True
while TC > 0:
    array = []

    for _ in range(n):
        array.append(random.randint(-30, 30))

    a, b = sorted(array), selection_sort(array, n - 1)

    if a != b:
        flag = False
        break

    TC -= 1

if flag:
    print("correctly Sorted!")

