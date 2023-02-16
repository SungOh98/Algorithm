def getEachTime(height, inventory):
    time = 0
    for i in range(n * m):
        # 만들려는 높이가 더 클 경우 -> 블록을 쌓기
        if board[i] < height:
            if inventory < height - board[i]:
                return float("inf")
            time += height - board[i]
            inventory -= height - board[i]
        else:
            time += 2 * (board[i] - height)
            inventory += board[i] - height
    return time


def main_func():
    minTime = float('inf')
    height = -float('inf')
    for k in range(257):
        tmpTime = getEachTime(k, b)

        if (tmpTime < minTime):
            minTime = tmpTime
            height = k

        elif minTime == tmpTime:
            if (k > height):
                height = k

    return f"{minTime} {height}"


import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
board = []
for i in range(n):
    board += list(map(int, input().split()))

board.sort(reverse=True)

print(main_func())
