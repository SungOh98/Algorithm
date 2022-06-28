# 숫자카드 2
# 상근이는 n개의 숫자카드를 가지고 있다.
# 정수 m개가 주어졌을 때, 이 수가 적혀있는 숫자카드를 상근이는 몇개를 가지고있을까
# 이전 풀이 >> 최악의 경우
import sys

iput = sys.stdin.readline

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
things = list(map(int, input().split()))

# target의 가장 오른쪽을 찾기 위한 이진 탐색 함수
'''
기존의 이진 탐색의 변형
기존의 이진 탐색에서 arr[mid] == target이면 결과를 return 하는데 반에
변형한 부분은 arr[mid] == target이라도 start값을 조정해주어 가장 오른쪽 target의 인덱스 값을 찾음
종료 조건은 start == end 일 경우, 즉 탐색 범위가 하나일 경우로 조정.
'''
def upper_target(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] > target:
        return upper_target(start, mid, arr, target)
    else:
        return upper_target(mid + 1, end, arr, target)

# target의 가장 왼쪽을 찾기 위한 이진 탐색 함수
def lower_target(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] >= target:
        return lower_target(start, mid, arr, target)
    else:
        return lower_target(mid + 1, end, arr, target)


def main_func():
    for num in things:
        print(upper_target(0, n, array, num) - lower_target(0, n, array, num), end=" ")


main_func()
