'''Parametric Search'''

'''
상근이는 나무 M미터가 필요하다. 나무 한줄에 대한 벌목허가를 받아
나무 한 줄을 새로 구입한 나무 절단기를 통해 M미터의 나무를 얻으려고 한다.
목재 절단기는 다음과 같이 동작한다.
1. 높이 H를 지정한다.
2. 톱날이 지면으로 부터 H만큼 올라간다.
3. 한줄에 연속해 있는 나무들을 절단한다.

이 목재 절단기를 가지고
적어도 M미터의 나무를 집에 가져가기 위한 절단기에서 설정할 수 있는 높이의 최댓값 H를 구하여라.

내 풀이

나무의 최소 길이 ~ 최대 길이 사이를 이진 탐색으로 돌려가며
중간 값에 대한 잉여 값을 확인

기존의 이진 탐색은 배열의 인덱스로 접근을 하였지만
이 문제는 인덱스의 값!! 으로 접근!

시간 복잡도
n * log m 

파라메트릭 서치의 활용
최적화 문제: 잘라야 하는 나무의 높이 H의 최댓값
결정 문제: 자르는 높이가 X일때, 얻을 수 있는 나무의 길이는 M 이상인가 아닌가?
주의 사항: 잘라야하는 높이는 감소함수 또는 증가함수 여야 이분 탐색이 가능하다!
따라서 파라메트릭 서치 풀이를 떠올릴 떄는
1. 최적화문제를 결정문제로 바꿀 수 있는 지 생각하고
2. 그 결정 문제로 얻어낸 함수가 감소또는 증가함수인지를 따져봐야 한다.

문제에서 최대 혹은 최소 얘기가 있으며 입력 범위가 무지막지하게 크다면 위 1, 2 번을 생각하며 파라메트릭 서치로 문제를 해결할 수 있을지
확인하는 통찰력이 필요하다!


'''


def get_surplus(arr, value):
    surplus = 0
    for i in range(len(arr)):
        tmp = arr[i] - value
        if tmp > 0:
            surplus += tmp

    return surplus


def binary_search(array, m):
    start, end = 0, max(array)
    # logm
    while start <= end:
        mid = (start + end) // 2
        # n
        surplus = get_surplus(array, mid)

        if surplus == m:
            return mid
        # 잉여값이 더 크다면 높이를 더 크게 조정
        elif surplus > m:
            start = mid + 1

        else:
            end = mid - 1

    return (start + end) // 2


n, m = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array, m))

'''
반례
6 12
19 9 18 20 17 8
ans : 15

3 1
1 2 2
ans : 1

'''
