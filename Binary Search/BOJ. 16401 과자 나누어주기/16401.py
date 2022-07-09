'''
조카들을 달래기 위해 홍익이는 막대과자를 하나씩 나누어준다.
조카들이 과자를 먹는동안 떼를 쓰지 않기 때문에 최대한 긴 과자를 나누어 주려고 한다.
그런데 나누어 준 과자의 길이가 다르다면 조카들이 화를 내기 때문에 똑같은 길이의 과자를 나누어 주어야 한다.
m명의 조카가 있고, n개의 과자가 있을 때, 조카 1명에게 줄 수 있는 과자의 최대길이를 구하여라.
단 막대과자는 길이와 상관없이 여러 조각으로 나누질 수 있지만, 과자를 하나로 합칠 수는 없다.

예제
4 3
10 10 15

15 짜리 과자를 7두개로 나누어 총 7길이의 과자 4개를 나누어 줄 수 있다.

최대 최소 문제 + 입력값이 무지막지하게 크다 >> 파라메트릭 서치 의심!

1. 최적화문제를 결정문제로 바꿀 수 있는가?
임의의 과자 길이 x에 대해서 나누어 줄 수 있는 과자의 갯수가 m 이상인가? 아닌가?
2. 임의의 과자 길이가 증가 / 감소 함수로 접근 가능한가? >> 증가함수로 접근 가능하다!



'''
# n의 시간 복잡도
def get_number(array, length):
    number = 0
    for i in range(len(array)):
        number += array[i] // length

    return number

def binary_search(array, m):
    start, end = 0, 1_000_000_000

    while start <= end:
        mid = (start + end) // 2

        if mid == 0:
            return 0

        number = get_number(array, mid)

        # 나누어 줄 수 있는 과자의 갯수가 기준 값보다 크거나 같다면
        if number >= m:
            # 과자의 크기를 늘리기.
            start = mid + 1
        # 나누어 줄 수 있는 과자의 갯수가 기준 값보다 작다면
        else:
            # 과자의 크기를 줄이기.
            end = mid - 1
    return (start + end) // 2

m, n = map(int, input().split())
array = list(map(int, input().split()))
print(binary_search(array, m))

