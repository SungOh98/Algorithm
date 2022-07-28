'''
두 배열의 합

두 배열의 부분 배열의 합이 T가 되는 경우의 수를 구하시오

입력의 크기가 1,000이므로
O(N^2 log N^2) 의 알고리즘 설계가 필요하다.

알고리즘
1. 두 배열의 subfix_sum 을 구한다. >> N
2. 각 subfix_sum의 모든 경우의 수를 담는 배열을 구한다 >> N^2
3. 이분 탐색을 위해 하나의 배열을 정렬 >> N^2 log N^2
4. 하나의 경우의 수 배열을 기준으로 원소를 하나씩 검사하며 >> N^2
    다른 경우의수 배열과의 합이 T가 되는 경우를 bisect로 찾는다 >> log N^2

시간 복잡도 > O(N^2 log N^2)
'''

def bisect_right(array, target):
    start, end = 0, len(array)

    while start < end:
        mid = (start + end) // 2

        if array[mid] <= target:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2

def bisect_left(array, target):
    start, end = 0, len(array)

    while start < end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2

def subfix_sum(arr):
    subfix = []
    # 그냥 누적합 배열 먼저 만들기

    tmp = 0

    for i in arr:
        tmp += i
        subfix.append(tmp)

    # 모든 부분 배열의 합을 담은 배열로 변환
    new_arr = subfix[:]
    for i in range(1, len(subfix)):
        for j in range(i):
            new_arr.append(subfix[i] - subfix[j])


    return new_arr


def main_func():
    answer = 0
    arr1 = subfix_sum(array1)
    arr2 = sorted(subfix_sum(array2)) # 이분 탐색을 진행할 배열

    for i in arr1:
        answer += bisect_right(arr2, T - i) - bisect_left(arr2, T - i)
    return answer



T = int(input())
n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

print(main_func())