'''
이미지 퀄팅
하나의 패턴 이미지를 여러개 이어 붙여서 큰 이미지를 만들어 내는 것
편의상 높이가 같은 두 이미지를 붙이는 방식만 활용
1. 두 이미지의 경계를 최소 2만큼 포갠다.
2. 포개어진 영역에서 두 이미지의 차이가 최소가 되도록 경계선을 결정한다.
3. 포개어진 영역에서 경계선과 경계선 오른쪽 부분을 오른쪽 이미지로 대체한다.

경계선 결정
1. 경계선은 포개어진 영역의 한 행마다 하나의 픽셀을 선택하여 생성한다.
2. 경계선의 각 행에 선택된 픽셀은 위 또는 아래 행에서 선택된 픽셀과 두칸 이상 떨어질 수 없다.

가장 자연스럽게 두 이미지를 이어 붙일 수 있는 경계를 선택하여야한다.
경계선의 부자연스러움의 정도: 경계선 픽셀에서 두 이미지의 픽셀의 색상 차의 제곱의 모든 합으로 정의

이 문제에서는 흑백 영상만을 다루므로
각 픽셀의 색상은 0~255의 정수형태로 표현된다.
두 이미지의 포개어질 영역의 색상값이 주어질 때 최적의 경계선이 가지는 부자연스러움 수치의 최소를 구하시오.

1. DP 테이블 정의
DP[i][j] : i행 j열 픽셀이 경계선의 일부 일때 최소 부자연스러움.
2. 점화식
DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - 1], DP[i - 1][j + 1]) + C(i, j)
-> C(i, j) : A[i][j] 와 B[i][j]가 포개져서 생기는 부자연스러움

'''
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
dp = [[0] * W for _ in range(H)]
for i in range(W):
    dp[0][i] = (A[0][i] - B[0][i]) ** 2

# for i in dp:
#     print(i)
if W > 1:
    for i in range(1, H):
        for j in range(W):
            if j == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + (A[i][j] - B[i][j]) ** 2
            elif j == W - 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + (A[i][j] - B[i][j]) ** 2
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + (A[i][j] - B[i][j]) ** 2
else:
    for i in range(1, H):
        dp[i][0] = dp[i - 1][0] + (A[i][0] - B[i][0]) ** 2

print(min(dp[-1]))