'''
Bubble Sort
현재 탐색 범위에서 가장 큰 원소를 계속 뒤로 보내는 알고리즘
뒤에서 부터 차례로 정렬이 완성됨
단위 연산을 비교 연산 으로 잡는다면
비교 연산 횟수: (n-1) + (n - 2) + ..... + (1) = {n*(n - 1)} / 2
time complexity = theta({n*(n - 1)} / 2) = theta(n^2)

개선된 버블 소트
bool 형 변수를 설정하여
j루프가 돌 동안 한번도 swap이 발생하지 않는다면 이미 정렬이 완료된 상태라고 판단하여 정렬을 끝낸다.
J루트가 돌 동안 한번도 swap이 발생하지 않았다는 의미는 이미 큰 수들이 뒤에 모두 배치되었다는 의미이다 즉 이미 정렬이 완료가 되었다는 얘기

기존의 버블 소트는 배열의 형태가 어떻든 비교횟수가 동일하였다 >> 세타(n^2)
개선된 버블 소트는 배열이 이미 정렬된 상태라면 단 한번의 배열 탐색으로 정렬을 끝낼 수 있다. >> 오메가(n), O(n^2)
'''
def Bubble_sort(arr: "정렬할 배열", n: "배열의 끝"):
    for i in range(n, 0, -1):
        flag = False
        # j 루프가 끝날 때마다 배열의 i 번째 원소는 자리 확정.
        for j in range(i):
            # 단위 연산 >> 비교문
            if arr[j] > arr[j + 1]:
                flag = True
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # swap이 한번도 발생하지 않았다면 종료!
        if not flag:
            break

    return arr


import random
# n = int(input("배열의 크기를 입력하세요: "))
n = 20
array = []

for _ in range(n):
    array.append(random.randint(-30, 30))

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
tmp = sorted(array)
print("<Sorted Array>\n", tmp)
bubble = Bubble_sort(array, len(array) - 1)
print("<Bubble Sort>\n", bubble)


if tmp == bubble:
    print("correctly sorted!")