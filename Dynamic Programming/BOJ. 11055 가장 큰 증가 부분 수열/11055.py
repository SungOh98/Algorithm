'''
1. dp 테이블 정의
dp[i] : i번 요소의 가장 큰 증가 부분 수열의 합
2. 점화식
dp[i] = max(dp[i], dp[j] + arr[i]) 단 j = 0...i - 1 에서 arr[i] > arr[j]를 만족하는 j
'''

n = int(input())
arr = list(map(int, input().split()))
dp = arr[:]
# O(N^2)
for i in range(n):
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))