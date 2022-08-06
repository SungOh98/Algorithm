'''
서버실
NxN 공간의 각 칸에 컴퓨터들이 쌓여 있다. >> 높이 1당 한대의 컴퓨터 최대 높이: 10,000,000 1 <= N <= 1000
냉방기의 차가운 공기는 1분당 1의 높이에 퍼진다.
각 컴퓨터는 냉방기의 공기가 닿아야 켜진다.
서버의 컴퓨터 중 절반 이상이 켜지려면 몇분이 필요할까?
O(N^2 log H)의 알고리즘 설계가 필요하다.

문제 정의: 서버의 컴퓨터들이 절반이상 켜지기 위한 최소 시간을 구하자.


'''

def is_over_half(x, arr, half, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
           cnt += min(x, arr[i][j])

    return cnt >= half

def parametric_search(arr, n):
    start, end = 0, 10_000_000
    numbers = sum([sum(k) for k in arr])

    while start < end:
        mid = (start + end) // 2

        if is_over_half(mid, arr, numbers / 2, n):
            end = mid
        else:
            start = mid + 1
    return (start + end) // 2

n = int(input())
server = [list(map(int, input().split())) for _ in range(n)]
print(parametric_search(server, n))
