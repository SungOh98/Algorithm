n = int(input("트리의 높이를 입력하세요: "))
tree = [["-"] * (2 ** n + 1) for _ in range(n)]

def dfs(row, left, right):
    if row >= n:
        return
    mid = (left + right) // 2
    tree[row][mid] = "X"
    dfs(row + 1, left, mid)
    dfs(row + 1, mid, right)

def print_board(board):
    for i in board:
        print("".join(i))
dfs(0, 0, 2 ** n)
print_board(tree)