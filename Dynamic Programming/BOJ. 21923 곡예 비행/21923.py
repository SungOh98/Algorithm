'''
곡예 비행
각 칸에 점수가 적힌 N * M 이차원 격자에서
비행하며 얻는 점수의 합으로 순위를 매김
비행 점수: 상승 비행할 때 지나간 칸에 부여된 점수의 총합 + 하강 비행할 때 지나간 칸에 부여된 점수의 총합
상승 비행 후 하강 비행함
상승 비행 중 앞 또는 위로만 이동 가능
하강 비행 중 앞 또는 아래로만 이동 가능

DP[i][j] = DP_UP[i][j] + DP_DOWN[i][j]
>>   DP_DOWN은 경로를 거꾸로 하면 되겠다!
DP_UP[i][j]

1. DP 테이블 정의
DP[i][j] : 시작 점으로부터 board[i][j] 까지 왔을 때 최대 점수
2. 점화식
DP_UP[i][j] += max(DP_UP[i + 1][j], DP_UP[i][j - 1])
DP_DOWN[i][j] += max(DP_DOWN[i + 1][j], DP_DOWN[i][j + 1])

DP[i][j] = DP_UP[i][j] + DP_DOWN[i][j]


'''

def take_off(dp):
    # 초기설정 >> 이것때문에 낮설음
    # 출발점을 포함한 행/ 열은 출발점으로부터 따로 갱신
    for i in range(1, m):
        dp[n - 1][i] += dp[n - 1][i - 1]
    for i in range(n - 2, -1, -1):
        dp[i][0] += dp[i + 1][0]
    # 점화식 도출
    for i in range(n - 2, -1, -1):
        for j in range(1, m):
            dp[i][j] += max(dp[i + 1][j], dp[i][j - 1])
    # for i in dp:
    #     print(i)

def land(dp):
    # 초기 설정
    # 출발점을 포함한 행/ 열은 출발점으로부터 따로 갱신
    for i in range(m - 2, -1, -1):
        dp[n - 1][i] += dp[n - 1][i + 1]
    for i in range(n - 2, -1, -1):
        dp[i][m - 1] += dp[i + 1][m - 1]
    # 점화식 도출
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            dp[i][j] += max(dp[i][j + 1], dp[i + 1][j])
    # for i in dp:
    #     print(i)
# 두 DP테이블의 요소들을 합한 각 요소중 최대값이 정답.
def answer(dp1, dp2):
    max_v = -float('inf')
    for i in range(n):
        for j in range(m):
            if max_v < dp1[i][j] + dp2[i][j]:
                max_v = dp1[i][j] + dp2[i][j]
    return max_v

def main_func(dp1, dp2):
    take_off(dp1)
    land(dp2)
    return answer(dp1, dp2)


n, m = map(int, input().split())
DP_UP = [list(map(int, input().split()))for _ in range(n)]
DP_DOWN = [x[:] for x in DP_UP]

print(main_func(DP_UP, DP_DOWN))