'''
1. DP 테이블 정의
두 문자열 S, T에 대해
DP[i][j] = 두 문자열 S[:i + 1], T[: j + 1] 의 LCS 길이 값.
2. 점화식
    s[i] == s[j] 일 경우
    dp[i][j] = dp[i - 1][j - 1] + 1
    s[i] != s[j] 일 경우
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
'''

S = " " + input()
T = " " + input()
dp = [[""] * (len(S)) for _ in range(len(T))]
for i in range(1, len(T)):
    for j in range(1, len(S)):
        if T[i] == S[j]:
            dp[i][j] = dp[i - 1][j - 1] + str(S[j])
        else:
            if len(dp[i][j - 1]) > len(dp[i - 1][j]):
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j]
print(len(dp[-1][-1]))
print(dp[-1][-1])
# for i in dp:
#     print(i)