'''
배양액을 뿌릴 수 있는 땅은 미리 정해져 있다.
배양액은 매초 이전에 배양액이 도달한적 없는 인접한 땅으로 퍼져나간다
황토색 칸이 배양액을 뿌릴 수 있는 칸임.
초록색 배양액과 빨간색 배양액이 동일한 시간에 도달한 땅에서 꽃이 피어난다.
꽂이 피어난 칸에는 더이상 배양액이 퍼져나가지 않는다.
정원의 정보와 배양액의 정보가 주어졌을 떄 피울 수 있는 꽃의 최대 개수를 출력하라.
0은 호수, 1은 배양액을 뿌릴 수 없는 칸 2는 배양액을 뿌릴 수 있는 칸.

알고리즘
1. 조합을 통해 배양액을 뿌릴 수 있는 경우의 수를 찾는다. >> 최대 경우의 수 >> 10 C 5 >>  252가지 경우의 수
>> 백트래킹으로 구현해보고 시간 내에 안되겠으면 조합 모듈 사용하자.
2. level 단위로 퍼뜨린다.
3. 퍼트린후 어떤 것을 큐에 넣을지 결정하고 큐에 다시 삽입

# 빨간색 >> 3
# 초록색 >> 4
# 꽃 >> 5

'''
from itertools import combinations
from collections import deque

'''호수: 0, 땅: 1~2, 초: 3, 빨: 4, 꽃: 5'''


def bfs(table, green, red):
    q = deque()

    for y, x in green:
        q.append((y, x, 3))
    for y, x in red:
        q.append((y, x, 4))

    ans = 0

    while q:
        cand = []
        for _ in range(len(q)):
            y, x, color = q.popleft()

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if (0 <= ny < n and 0 <= nx < m) and 1 <= table[ny][nx] <= 2:
                    cand.append((ny, nx, color))

        cand = set(cand)
        for y, x, color in cand:
            if 1 <= table[y][x] <= 2:
                table[y][x] = color
            else:
                table[y][x] = 5
                ans += 1
        for y, x, color in cand:
            if table[y][x] != 5:
                q.append((y, x, color))
    return ans


def make_table(red, green):
    table = [x[:] for x in garden]
    for y, x in green:
        table[y][x] = 3
    for y, x in red:
        table[y][x] = 4
    return table


def main_func(idx, depth, green, avail, garden):
    global answer
    if depth == g:

        tmp = list(set(avail) - set(green))
        reds = list(combinations(tmp, r))
        for red in reds:
            red = list(red)
            table = make_table(red, green)
            answer = max(answer, bfs(table, green, red))

        return

    for i in range(idx, len(avail)):
        main_func(i + 1, depth + 1, green + [avail[i]], avail, garden)


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n, m, g, r = map(int, input().split())
garden = []
available = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(m):
        if a[j] == 2:
            available.append((i, j))
    garden.append(a)
answer = 0
main_func(0, 0, [], available, garden)
print(answer)

