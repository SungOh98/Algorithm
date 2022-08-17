'''
메탈
N개의 메탈이 존재
K개의 horizontal tunnel 을 생성하여 N개의 metal을 채굴하려고 한다.
cost는 max(horizontal tunnel 으로 부터 metal(i)까지의 거리)

cost의 최소값을 구하여라.

임의의 cost X를 정한다.
X로 모든 광물을 채굴할 수 있다면 X를 줄인다.
채굴할 수 없다면 X를 늘린다.

y좌표는 항상 정수만 입력 받는다.
따라서 cost는 소수점 첫째자리까지 나오는게 자명하다.
이분 탐색을 원활히 진행하기 위해 10을 곱해주고 진행한 후 정답에 10을 나눠주자.
이분 탐색은 정수 범위에서 진행해야하기 때문이다.

'''


def is_possible(coordinates, k, cost):
    _min, _max = float('inf'), -float('inf')
    k -= 1
    for x, y in coordinates:
        _min = min(_min, y)
        _max = max(_max, y)
        if abs(_max - _min) / 2 > cost:
            _min, _max = y, y
            k -= 1
    return k >= 0

def parametric_search(coordinates, k):
    start, end = 0, int(2e9)
    answer = 0
    while start < end:
        mid = (start + end) // 2
        if is_possible(coordinates, k, mid):
            end = mid
            answer = mid

        else:
            start = mid + 1
    return answer / 10

import sys
input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    n, k = map(int, input().split())
    coordinates = []
    a = list(map(int, input().split()))
    for i in range(0, len(a), 2):
        coordinates.append((a[i] * 10, a[i + 1] * 10))
    # x좌표 기준 정렬
    coordinates.sort(key=lambda x: x[0])
    # print(is_possible(coordinates, k, 0))
    print(parametric_search(coordinates, k))