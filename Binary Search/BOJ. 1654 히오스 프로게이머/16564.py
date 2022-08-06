'''
히오스 프로게이머
n개의 캐릭터와 각 캐릭터의 레벨이 주어진다.
총 레벨을 K만큼 올릴수 있다.
팀 목표레벨을 캐릭터들의 최소레벨이라 정의할때
달성할 수 있는 최대 팀 목표레벨을 몇인가?

임의의 팀 목표레벨이 X로 맞출 수 있는가?
있다면 >> 늘리기
없다면 >> 줄이기
'''

def is_possible(x, arr, m):
    for i in arr:
        # 해당 캐릭터의 레벨이 임의의 X보다 작다면
        if i < x:
            m -= (x - i)

    return m >= 0

def parametric_search(arr, m):
    start, end = 1, 2_000_000_000

    while start <= end:
        mid = (start + end) // 2

        if is_possible(mid, arr, m):
            start = mid + 1

        else:
            end = mid - 1

    return (start + end) // 2

n, k = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
print(parametric_search(array, k))