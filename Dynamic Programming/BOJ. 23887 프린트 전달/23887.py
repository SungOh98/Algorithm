from collections import deque


def print_board(board):
    for i in board:
        print(i)
    print()

def dfs(graph, root, visit, dp):

    visit[root] = True

    for i in graph[root]:
        if visit[i]:
            continue
        dp[root] += dfs(graph, i, visit, dp)

    return dp[root]

def bfs(visited, start):
    s_y, s_x = start[0], start[1]
    visited[s_y][s_x] = 0
    q = deque([(s_y, s_x, 1, 0)])
    graph = [[] for _ in range(k + 1)]
    parent = [int(1e9)] * (k + 1)
    while q:

        y, x, depth, prev_node = q.popleft()

        if parent[board[y][x]] <= prev_node:
            continue

        parent[board[y][x]] = prev_node

        for i in range(8):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] > 0 and visited[ny][nx] >= depth:
                    visited[ny][nx] = depth
                    q.append((ny, nx, depth + 1, board[y][x]))
    for i in range(1, k + 1):
        if parent[i] == int(1e9):
            return -1
        graph[parent[i]].append(i)
    return graph

def main_func(start):
    dp = [1] * (k + 1)
    visited = [False] * (k + 1)
    graph = bfs([[float('inf')] * m for _ in range(n)], start)
    if graph == -1:
        return -1
    dfs(graph, start_node, visited, dp)
    return " ".join(map(str, dp[1:]))


dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, -1, 1, -1, 1, -1, 1]
import sys
sys.setrecursionlimit(30000)
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for i in range(1, k + 1):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = i
start_node = int(input())
start = -1
for i in range(n):
    for j in range(m):
        if start_node == board[i][j]:
            start = (i, j)
            break
print(main_func(start))