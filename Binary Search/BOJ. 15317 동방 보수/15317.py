'''
동방 보수

1 <= N <= 100,000 개의 동방과 각 동방의 보수비용 N(i) 가 있다.
1 <= M <= 100,000 개의 동아리와 각 동아리 당 예산 M(i) 가 있다.
K원을 동아리들에게 지원한다.

하나의 동아리는 하나의 동방을 차지할 수 있다.
차지할 수 있는 동방의 최대개수를 구하시오.

Parametric Search로 임의의 동방의 개수 X를 정한다.
X개의 동방을 보수할 수 있는가?
있다면 >> 늘려
없다면 >> 줄여

결정함수 : X개의 동방을 보수할 수 있는가 만 결정하면 된다.
당연히 보수 비용이 적은 동방들을 취하는게 좋다.
또한 동아리들은 예산이 많은 순서대로 고르는게 좋다.
반드시 X개의 동방은 결정해야한다.
따라서 예산이 많은 동아리 방부터 고른 X개의 동방 중 보수 비용이 많은 동방끼리 매칭 시킨다.
x개의 동방중 보수 비용의 최대값 - 예산이 가장 많은 동아리
...
x개의 동방중 보수 비용의 최소값 - 예산이 X번째로 많은 동아리
'''

def is_possible(x, room, group, supply):
    if x > len(room) or x > len(group):
        return False
    room = room[:x]
    group = group[len(group) - x:]
    for i in range(x):
        supply -= room[i] - group[i] if room[i] > group[i] else 0
    return supply >= 0

def parametric_search(r, g, s):
    start, end = 0, 100_000
    while start <= end:
        mid = (start + end) // 2

        if is_possible(mid, r, g, s):
            start = mid + 1
        else:
            end = mid - 1
    return (start + end) // 2
import sys
input = sys.stdin.readline
n, m, k = map(int ,input().split())
rooms = sorted(list(map(int, input().split())))
groups = sorted(list(map(int, input().split())))
print(parametric_search(rooms, groups, k))