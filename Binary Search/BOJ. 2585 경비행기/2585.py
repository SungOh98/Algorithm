'''
경비행기
출발지 S에서 목적지 T까지 빠른 속도로 이동하려고 한다.
연료통의 크기를 결정하는게 문제임
큰 연료통 >> 급유 횟수는 줄지만 무거워서 속도가 느려짐
작은 연료 >> 급유 횟수 큼, 속도 빠름
문제: 급유횟수가 K이하일 때 연료통의 최소용량을 구하는 것
1L당 10KM 감
두 지점까지의 직선거리: 두 점사이의 거리 공식
출발지 : (0, 0)
도착지: (10000, 10000)

3 <= 출발지와 목적지를 제외한 비행장 수 <= 1000
0 < x, y < 10000 : 출발지와 도착지를 제외한 비행장의 x, y좌
0 <= K(급유 가능 횟수) <= 1000

파라메트릭 서치 문제 해결법
1. 최적화 문제를 결정문제로 바꿀 수 있는가? : 임의의 용량 X로 출발지로부터 목적지까지 갈 수 있는가? 로 변경!
>> 갈 수 있다면 줄여
>> 갈 수 없다면 늘려
2. 단조성을 확인한다. -> ok

결정함수: 임의의 용량 X의 연료통과 K번의 급유횟수로 출발지에서 목적지까지 갈 수 있는가? 를 확인해야함.
단순히 생각해보았을 때 n이 1000이하이므로
 0. fully connected graph를 구성하고
 1. 결정함수를 bfs로 돌리면 될 듯
    다음 노드사이의 거리를 용량 X로 가지 못하면 큐에 삽입 안함
    도착 노드에 도착했을 때 급유 횟수 K보다 작은 경우가 있다면 True를 리턴

'''

import math
from collections import deque
import sys
class Sol:
    def __init__(self, c, n, k):
        self.coordinates = [[0, 0]] + c + [[10000, 10000]]
        self.graph = [[] for _ in range(len(self.coordinates))]
        self.n = n + 2
        self.k = k
        self.answer = 0
        # print(self.coordinates)

    # Fully connected Graph 만들기
    def make_graph(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    dist = math.sqrt((self.coordinates[i][0] - self.coordinates[j][0]) ** 2 + (self.coordinates[i][1] - self.coordinates[j][1]) ** 2)
                    self.graph[i].append([j, dist])

        # for i in range(self.n):
            # print(self.graph[i])

    def bfs(self, x):
        q = deque()
        visited = [False] * self.n
        visited[0] = True
        q.append((0, 0))

        while q:
            node, depth = q.popleft()
            # 도착노드이면서 경유 횟수가 K이하라면
            if node == self.n - 1 and depth - 1 <= self.k:
                return True

            for adj_n, adj_w in self.graph[node]:
                # 방문하지 않고 경유 X로 갈수 있는 노드라면
                if not visited[adj_n] and adj_w <= x * 10:
                    visited[adj_n] = True
                    q.append((adj_n, depth + 1))

        return False

    def parametric_search(self):
        # 최대 연료통의 크기는 10000 * 10000
        start, end = 0, 100_000_000
        while start < end:
            mid = (start + end) // 2

            if self.bfs(mid):
                end = mid
            else:
                start = mid + 1
        self.answer = (start + end) // 2

def main_func():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    c = []
    for _ in range(n):
        c.append(list(map(int, input().split())))
    play = Sol(c, n, k)
    play.make_graph()
    play.parametric_search()
    return play.answer
print(main_func())