'''
n* m 격자에 미로가 존재
(x, y)에서 출발하여 (r, c)로 탈출해야한다.

탛출 조건
1. 격자의 바깥으로 나갈 수 없다.
2. (x, y)에서 (r, c)까지 이동하는 거리가 총 k여야한다.
 >> 같은 격자를 두번 이상 방문해도 된다.
3. 미로에서 탈출한 경로를 문자열로 나타내었을 때 문자열이 사전순으로 가장 빠른 경로로 탈출해야한다.
이동 경로는 다음과 같이 문자열로 바꿀 수 있다.
l: 왼쪽으로 한칸 이동
r: 오른쪽으로 한칸 이동
u: 위쪽으로 한칸 이동
d: 아래쪽으로 한칸 이동

예를 들어 왼쪽 한칸, 위로한칸 왼쪽 한칸 이동했다면 lul임,

상하좌우 인접 격자 한칸 씩 이동 가능
.은 빈공강
s: 출발점
e: 도착점

도착점에 도달한다고 해서 바로 종료되는 것은 아님.
미로를 탈출할 수 없다면 impossible 출력

2 <= n <= 50
2 <= m <= 50
출발점과 도착점이 같은 경우는 주어지지 않음
1 <= k <= 2500

도달할 수 없는 경우 > 만약 최단 경로가 짝수라면 홀수번째는 도착 불가
뭔가 다익스트라 같다.

도착지점의 문자열의 길이는 k여야함.
'''
'''
test
a = ["aaaa", "z", "aaab"]
b = ["l", "r", "u", "d"]
b.sort()
a.sort()
print(a)
print(b)

import heapq

c = []
heapq.heappush(c,"aa")
heapq.heappush(c,"z")
heapq.heappush(c,"k")
heapq.heappush(c,"a")

while c:
    tmp = heapq.heappop(c)
    print(tmp)
    
알고리즘
dist[i][j][k]: (i, j)에 k번 만에 도착한 문자열의 최소값
문자열의 최소값은 사전순
'''
import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
ds = ["u", "d", "l", "r"]


def dijkstra(dist, y, x, r, c, n, m, k):
    pq = []
    heapq.heappush(pq, ("", y, x, 0))

    while pq:
        str, y, x, depth = heapq.heappop(pq)
        # 갱신되지 않은 정보라면 무시
        if str > dist[y][x][depth]:
            continue
        # 문자열 길이가 k를 넘어서면 무시
        if depth >= k:
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if dist[ny][nx][depth + 1] > str + ds[i]:
                    dist[ny][nx][depth + 1] = str + ds[i]
                    heapq.heappush(pq, (str + ds[i], ny, nx, depth + 1))
    return "impossible" if dist[r][c][k] == "z" else dist[r][c][k]

def solution(n, m, x, y, r, c, k):
    dist = [[['z'] * (k + 1) for _ in range(m)] for _ in range(n)]
    return dijkstra(dist, x - 1, y - 1, r - 1, c - 1, n, m, k)

print(solution(3, 4, 2, 3, 3, 1, 5))
