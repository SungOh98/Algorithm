'''
Quick sort -> right pivot quick sort
주어진 배열을 두개로 분할하고 각각을 정렬하는 알고리즘.
병합정렬은 무식하게 두 부분으로 나누는 반면 퀵정렬은 pivot을 중심으로 pivot보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 위치시킴
즉, 분할 과정에서 정렬이 진행됨. (병합 정렬은 분할과정은 무식하게 나누기만하고 병합과정에서 정렬이 발생)

시간 복잡도 분석
1. partition 함수 시간 복잡도 분석(피벗 기준으로 왼쪽 오른쪽으로 원소를 위치시키는 함수)
: 현재 탐색 중인 크기의 배열만큼 탐색함 >> 빅오 표기법으로 표현하면 초기 배열의 길이가 n이라면 세타(n)

2. quick_sort() 함수 시간 복잡도 분석
: 최악의 경우는 배열이 초기 내림차순/ 오름차순으로 정렬되어 있을 경우이다.
이 경우, 배열의 모든 원소들이 피벗으로 한번씩 설정이 되며 quick_sort() 함수도 n번 호출하게 됨
재귀식: T(n) = T(n - 1) + n - 1 (n - 1은 partition 함수의 복잡도)
반복 대치를 통한 복잡도 산출은 세타(n^2)
평균의 경우는 재귀식: T(n) = T(n - i) + T(i - 1) + n - 1
복잡도: 세타(Nlogn)

따라서 quick_sort()의 시간 복잡도는 최악의 경우 세타(n^2) 평균의 경우 세타(nlogn)의 복잡도를 보장한다.
또한 정렬이 필요한 일반적인 경우, quick_Sort알고리즘의 최악의 경우인 상황이 드물기 떄문에 quick_sort는 일반적인 경우 높은 성능을 보장한다.

'''

def partition(arr, start, end):
    pivot = end
    #  투 포인터 i, j
    i, j = start - 1, start

    while j < end:
        if arr[j] <= arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
    arr[pivot], arr[i] = arr[i], arr[pivot]

    return i

def Quick_Sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        Quick_Sort(arr, start, pivot - 1)
        Quick_Sort(arr, pivot + 1, end)

if __name__ == "__main__":

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
        Quick_Sort(array, 0, n - 1)

        if Test != array:
            flag = False
            break

        TC -= 1

    if flag:
        print("correctly Sorted!")

