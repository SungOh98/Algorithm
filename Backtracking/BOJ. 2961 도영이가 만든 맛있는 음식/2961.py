'''
1 <= N <= 10
백 트래킹
'''


def backtracking(idx, sour, bitter, choice):
    global ans
    if idx == n:
        if choice:
            ans = min(abs(sour - bitter), ans)
        return

    backtracking(idx + 1, sour * foods[idx + 1][0], bitter + foods[idx + 1][1], True)
    backtracking(idx + 1, sour, bitter, choice)



ans = float('inf')
n = int(input())
foods = [[0, 0]]
for _ in range(n):
    foods.append(list(map(int, input().split())))
backtracking(0, 1, 0, False)
print(ans)

