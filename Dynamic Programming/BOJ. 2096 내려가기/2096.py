import sys
input = sys.stdin.readline
n = int(input())
tmp = list(map(int, input().split()))
tmp2 = tmp[:]

for _ in range(n - 1):
    dp = list(map(int, input().split()))
    dp2 = dp[:]
    dp[0], dp2[0] = max(tmp[0], tmp[1]) + dp[0], min(tmp2[0], tmp2[1]) + dp2[0]
    dp[1], dp2[1] = max(tmp[0], tmp[1], tmp[2]) + dp[1], min(tmp2[0], tmp2[1], tmp2[2]) + dp2[1]
    dp[2], dp2[2] = max(tmp[2], tmp[1]) + dp[2], min(tmp2[2], tmp2[1]) + dp2[2]
    tmp, tmp2 = dp, dp2
print(f"{max(tmp)} {min(tmp2)}")
