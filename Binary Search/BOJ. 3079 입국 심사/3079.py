'''
입국 심사
M명의 사람이 일렬로 서서 입국 심사를 기다리고 있다.
입국 심사대는 N
K번 심사대에 한명을 입국 심사하는 데 걸리는 시간 Tk
초기 모든 심사대는 비어있으며
하나의 심사대 당 한명씩만 할 수 있음

가장 앞에 서있는 사람이 비어있는 심사대가 보이면 가서 심사를 받으면 된다.
하지만 항상 이동해야하는 것은 아니며 더빠른 입국 심사를 기다렸다가 그곳으로 가도 된다.

상근이는 모든 사람이 입국 심사를 받는 데 걸리는 최소 시간을 구하려고 한다

제약 조건 : 1 <= N <= 100,000   1 <= M <= 1,000,000,000

O(N log M) 알고리즘 설계가 필요하다.

파라메트릭 서치
1. 최적화 문제를 결정문제로 바꿀 수 있는가?
최적화 : 모든 사람이 입국심사하는데 걸리는 최소 시간을 구하시오
결정 : 임의의 시간 X안에 모든 사람이 입국 심사를 할 수 있는가 ?
    > yes or no

O(N) 으로 임의의 시간 X 안에 모든 사람이 입국 심사를 받을 수 있는 알고리즘을 짜는게 관건...
>> 그리디!

시간이 적게 드는 심사대를 우선적으로 활용해야한다.

'''


def is_possible(arr, x, m):
    for i in arr:
        # 입국 심사해야할 모든 사람 수 -= 주어진 시간 X에 i번 심사대에서 처리할 수 있는 사람 수
        m -= x // i
        # 모든 사람을 처리했다면 True 리턴
        if m <= 0:
            return True
    # 사람이 남아있다면 False 리턴
    return False


def parametric_search():
    start, end = 1, int(1e18)

    while start < end:
        parameter = (start + end) // 2
        # 가능하다면 >> 파라미터를 줄이자
        if is_possible(array, parameter, m):
            end = parameter
        # 가능하지 않다면 >> 파라미터를 늘리자
        else:
            start = parameter + 1

    return (start + end) // 2


n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
# 정렬해주어 시간이 적게드는 입국 심사대 부터 채우기 ! > 그리디
array.sort()
print(parametric_search())