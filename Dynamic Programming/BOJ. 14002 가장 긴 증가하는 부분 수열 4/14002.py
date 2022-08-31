'''
1. dp테이블 정의
dp[i] 는 i번째 요소의 가장 긴 증가 부분 수열
2. 점화식
dp[i] = max(dp[i], dp[j] + arr[i])
'''
n = int(input())
array = list(map(int, input().split()))
dp = [[] for _ in range(n)]
for i in range(n):
    dp[i].append(array[i])
max_len = 0
max_idx = 0
for i in range(n):
    for j in range(i - 1, -1, -1):
        if array[i] > array[j]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [array[i]]
    if max_len < len(dp[i]):
        max_len = len(dp[i])
        max_idx = i
print(max_len)
print(" ".join(map(str, dp[max_idx])))

