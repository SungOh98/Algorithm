'''
Heap Sort

먼저 heap 자료구조에 대해 알아보자.
heap 자료구조는 완전 이진 트리이다. 또한 heapness 특성을 가진다.
heap 자료구조의 특징(min heap 기준)
1. heapness : 부모노드가 자식 노드보다 작은 key값을 가짐
2. completeness: 트리의 자식노드는 왼쪽 자식노드부터 차례로 채워진다. 왼쪽부터 오른쪽으로 빈공간 없이 차례로 채워진다.

이러한 completeness 특성 덕분에 heap 자료구조는 트리 자료 구조임에도 불구하고 하나의 배열로 표현할 수 있다.
각 노드를 배열의 인덱스로 접근할 수 있다.
어떤 노드의 인덱스를 k라하면
그 노드의 왼쪽 자식의 인덱스는 2k
그 노드의 오른쪽 자식의 인덱스는 2k + 1 이 된다.

따라서 어떤 정렬되어 있지 않은 배열이 들어오게 되면 자연스럽게 완전 이진트리를 구성할 수 있고
heapness 특성을 만족하게 조정만 해준다면 heap자료구조를 만들 수 있다.


heap 구성

'''

# tree의 높이만큼 수행 >> 세타(logn)
def heapify(arr, idx, n):
    left, right = 2 * idx, 2 * idx + 1
    # 해당 노드의 자식이 두개일 경우
    if right <= n:
        # 두 자식 중 작은 놈을 골라
        if arr[left] < arr[right]:
            smaller = left
        else:
            smaller = right
    # 자식이 하나일 경우
    elif left <= n:
        smaller = left
    # 자식이 없을 경우
    else:
        return

    # 부모보다 자식이 더 작을 경우
    if arr[idx] > arr[smaller]:
        # heapness 를 만족시키기 위해 swap
        arr[idx], arr[smaller] = arr[smaller], arr[idx]
        # 바꾼 자식 노드를 기준으로 재귀호출
        heapify(arr, smaller, n)

# 세타((n / 2) * logn) == 세타(nlogn)
def build_heap(arr, n):
    # 초기 배열의 전체 갯수의 반만큼 heapify 수행
    for i in range(n // 2, 0, -1):
        heapify(arr, i, n)
# 내림차순 정렬
def Heap_Sort(arr):
    tmp = [-1] + arr
    n = len(tmp) - 1
    build_heap(tmp, n)

    for i in range(n, 0, -1):
        tmp[i], tmp[1] = tmp[1], tmp[i]
        heapify(tmp, 1, i - 1)
    tmp.pop(0)
    return tmp






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

    Test = sorted(array, reverse=True)
    result = Heap_Sort(array)

    if Test != result:
        flag = False
        break

    TC -= 1

if flag:
    print("correctly Sorted!")
