'''
Insertion sort

배열의 1번째 원소부터 왼쪽으로 탐색을 시작하여 해당 원소를 삽입할 자리에 삽입하는 알고리즘
앞선 두 정렬과는 다르게 배열의 앞쪽부터 정렬이 완료된다. (물론 앞선 두 알고리즘들도 앞쪽부터 완료되게 만들 수 있다.)

매번 삽입할 원소를 선택 후 삽입할 자리를 찾기 위해 해당 원소의 앞 부분을 탐색할 시, 해당 원소의 앞 부분은 이미 정렬이 완료된 상태이다.(핵심)
따라서 만약 삽입할 원소가 앞 부분의 원소들 중 마지막 원소 보다 크다면 더이상 탐색을 할 필요가 없이 자리가 확정 된다.
이러한 결과 덕분에 만약 배열이 이미 정렬된 배열이라면 각각의 삽입할 원소를 선택함과 동시에 자리가 확정되므로 연산 횟수가 n-1 번이 된다
따라서 time complexity 는 omega(n), O(n^2)의 시간복잡도를 보장 한다.

삽입정렬의 최악의 경우는 배열이 내림차순으로 정렬 되어 있을 경우 이며, 선택 정렬과 동일한 연산 횟수를 수행하게 된다.
따라서 O(n^2)


'''
def insertion_sort(arr, n: "배열의 마지막 인덱스"):
    # 배열의 삽입할 원소들 = arr[i]
    for i in range(1, n):
        for j in range(i, 0, -1):
            # 뒤의 것이 앞의 것보다 작다면 swap
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            # 뒤의 것이 앞의 것보다 크거나 같다면 swap을 멈춤 >> 이미 앞의 것들은 정렬 되어 있으므로 자리가 확정!
            else:
                break
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

    a, b = sorted(array), insertion_sort(array, n)

    if a != b:
        flag = False
        break

    TC -= 1

if flag:
    print("correctly Sorted!")
