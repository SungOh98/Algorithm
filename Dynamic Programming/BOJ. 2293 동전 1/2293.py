'''
N종류의 가치가 서로 다른 동전으로 K원을 만들 고 싶다. 그 경우의 수는?
1. DP테이블 정의
    DP[i][j] 는 i종류의 동전으로 j원을 만드는 경우의 수
2. 점화식
    i = 1 2 3 ... N
    j = 1 2 3 ... K
    만약 W(i) > j 일 경우
        DP[i][j] = DP[i - 1][j]
    만약 W(i) <= J일 경우
        DP[i][j] = DP[i - 1][j] + DP[i][j - W(i)]
메모리 초과 풀이



DP = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    DP[i][0] = 1

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if weight[i] > j:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = DP[i - 1][j] + DP[i][j - weight[i]]
print(DP[-1][-1])
'''
N, K = map(int, input().split())
weight = [0]
for _ in range(N):
    weight.append(int(input()))
DP = [1] + [0] * K

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if weight[i] <= j:
            DP[j] += DP[j - weight[i]]
print(DP[-1])