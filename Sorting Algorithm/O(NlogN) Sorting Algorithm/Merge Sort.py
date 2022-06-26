# coding=utf-8
'''
Merge Sort

원소가 한 개 일때까지 현재 배열을 두 부분으로 분할.
한개까지 분할하면 병합 시작! >> merge 함수
병합 정렬의 핵심은 병합시 나누어진 두 배열이 이미 정렬이 되어있다는 것이다.
나누어진 두 배열이 이미 정렬이 되어 있기 떄문에 n의 시간 복잡도로 두 배열을 합칠 수 있다.

시간 복잡도 분석
1. merge함수의 시간 복잡도 분석
 >> 현재 탐색 배열의 범위 가 n이라 가정한다면 약 2*n의 연산을 수행! 따라서 세타(n)으로 퉁칠 수 있다.
2. merge sort의 시간 복잡도 분석
(쉽게 생각) 배열을 2부분으로 계속 나누어 가므로 >> 상태 공간 트리의 높이만큼 연산을 수행한다고 볼 수 있다.
>> logn 만큼의 연산 * n(merge 함수 연산) >> 총 세타(nlogn)의 시간 복잡도를 보장.

(재귀적 관계식)
T(n) = 2 * T(n / 2) + n(merge) : 두 부분으로 나누어 재귀 호출하므로 이런식으로 재귀적 관계식을 세울 수 있다.
이 관계식의 마스터 정리 / 반복 대치를 활용하여 구한 시간 복잡도 >> theta(nlogn)
'''

def merge(start, mid, end, arr):
    i, j, k = start, mid + 1, 0
    # i는 왼쪽 배열의 포인터
    # j는 오른쪽 배열의 포인터
    # k는 임시 배열의 포인터
    tmp = [0] * (end - start + 1)

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1

        else:
            tmp[k] = arr[j]
            k += 1
            j += 1

    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1

    while j <= end:
        tmp[k] = arr[j]
        k += 1
        j += 1

    # 여기까지 현재 탐색배열 범위만큼 연산

    # 이부분은 임시 배열에서 원래 배열로 복사 >> n 만큼의 연산
    k = start
    for i in tmp:
        arr[k] = i
        k += 1


def Merge_Sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        Merge_Sort(arr, start, mid)
        Merge_Sort(arr, mid + 1, end)
        merge(start, mid, end, arr)

# 정렬 테스트
import random
TC = int(input())
n = 20
# n = int(input("배열의 크기를 입력하세요: "))
flag = True
while TC > 0:
    array = []

    for _ in range(n):
        array.append(random.randint(-30, 30))

    Test = sorted(array)
    Merge_Sort(array, 0, n - 1)

    if Test != array:
        flag = False
        break

    TC -= 1

if flag:
    print("correctly Sorted!")