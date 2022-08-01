'''
처리해야할 동일한 작업 n개, 작업을 처리할 CPU 존재
CPU는 여러개의 코어가 있고 코어별 작업 처리시간이 다르다.
2개이상의 코어가 놀고있다면 앞의 코어부터 작업을 할당 받음
마지막 작업을 처리하는 코어를 출력하시오

2 <= M(코어의 수) <= 10000
코어당 처리시간 k <= 10,000
N <= 50,000

1. 임의의 시간 X를 (start + end) // 2로 구함
2. 임의의 시간 X동안 모든 작업을 처리할 수 있는지를 확인
    처리할 수 있다면 X = end 로 조정
    처리할 수 없다면 X = start + 1 로 조정
모든 작업을 완료하는 시간 X를 구하고 마지막으로 작업을 수행하는 코어의 번호를 출력한다.

O(M log kN) 의 알고리즘을 설계해야 효율성 검사를 통과할 수 있음
따라서 임의의 시간 X에 대해 모든 작업을 처리할 수 있는지 여부를 O(M) 안에 해결해야함.
https://www.acmicpc.net/problem/1561 와 매우 비슷
'''

def is_possible(arr, x, n):
    # O(M)
    for core in arr:
        # 임의의 시간 x동안 core가 처리한 작업의 수는 x를 core의 처리 시간 으로 나눈 몫 + 1(0초에 작업)임
        n -= x // core + 1

    # 모든 작업을 처리했다면
    if n <= 0:
        return True
    # 모든 작업을 처리하지 못했다면
    else:
        return False

def find_last_scheduled_core(arr, x, n):
    # 완료시각 -1 까지 처리되고 남은 작업의 개수를 구함
    last_num = n
    for core in arr:
        last_num -= (((x - 1) // core) + 1)
    # 남은 작업을 처리해주며 마지막 처리 코어를 리턴
    for i in range(len(arr)):
        if x % arr[i] == 0:
            last_num -= 1
            # 모두 처리했다면 처리한 코어 리턴
            if last_num <= 0:
                return i + 1


def parametric_search(arr, n):
    # 코어수가 1개이고 나머지가 모두 최대 값이라면 최대처리 시간은 50000 * 10000
    start, end = 1, 10
    while start < end:
        mid = (start + end) // 2
        # 임의의 mid 시간에 모든 작업을 처리할 수 있다면
        if is_possible(arr, mid, n):
            # 다음 mid값 조정
            end = mid
        else:
            start = mid + 1

    min_time = (start + end) // 2
    return find_last_scheduled_core(arr, min_time, n)

def solution(n, cores):
    answer = parametric_search(cores, n)
    return answer

print(solution(6, [1, 2, 3]))