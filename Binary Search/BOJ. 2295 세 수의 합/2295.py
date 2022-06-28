'''
세 수의 합
n개의 자연수들로 이루어진 집합 s가 있다.
이 중에서 세 수를 고르고 그 세수의 합이 여전히 집합 s에 있는 경우가 있다.
이런 경우들 중 가장 큰 세수의 합 d를 찾으라.
입력으로 받는 수들은 모두 다른 숫자들 이다.
세수는 같아도 된다.
5 <= N <= 1000
baaarking dog님의 영상 참고 풀이

arr[i], arr[j], arr[k] 의 합을 찾는 문제에서
arr[i]와 arr[j]의 합을 미리 구성해 놓은 temp 배열을 만들어
temp 에서 이분 탐색을 진행하여 arr[l] - arr[k] 값이 있는지 변형하는 것이 핵심 아이디어
( arr[k] + temp[i] 가 arr의 원소중 하나에 있다면 성공이므로! )
'''
# 두개씩 미리 더해 놓은 배열을 생성
def make_new_arr(arr):
    temp = set()
    for i in range(n):
        for j in range(i, n):
            temp.add(arr[i] + arr[j])
    temp = sorted(temp)
    return temp

def binary_search(array, start, end, target):
    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == target:
        return True

    elif array[mid] > target:
        return binary_search(array, start, mid - 1, target)

    else:
        return binary_search(array, mid + 1, end, target)


def main_func():
    # n^2
    new_arr = make_new_arr(arr)
    # n^2
    for i in range(n - 1, -1, -1):
        for j in range(n):
            # logn
            if binary_search(new_arr, 0, len(new_arr) - 1, arr[i] - arr[j]):
                return arr[i]
    # total = O{(n^2) log n}
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(main_func())
