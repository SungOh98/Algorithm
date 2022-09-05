'''
전깃줄
두 전봇대 사이 전깃줄이 있다.
이들 중 몇개의 전깃줄을 없애 전깃줄이 서로 교차되지 않도록 만들려고 한다.
전깃줄은 전봇대의 위에서부터 1번
없애야 하는 전깃줄의 최소 개수를 구하시오
1 <= 전깃줄의 개수 N <= 100
1 <= 전깃줄의 위치 <= 500
같은 위치에 두개 이상의 전깃줄은 연결 안됨.

Dynamic Programming
>> 부분 문제의 해답을 이용하여 전체문제의 해답을 도출한다.
어떻게 활용할지 잘 생각하여 점화식을 세우자.
전봇대 A만 고려해보자 어차피 일대일 함수 처럼 하나의 화살만 간다.
전봇대 A에서 뻗어나가는 전깃줄이 증가하는 형태이면 된다.
>> 가장 긴 증가 부분 수열 T를 찾고 N - T가 answer

DP[i] = max(DP[i], DP[j] + 1) j = 0 1 2 ... i - 1
'''
N = int(input())
lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))
lines.sort(key=lambda x: x[0])
DP = [1] * N
for i in range(N):
    for j in range(i - 1, -1, -1):
        if lines[i][1] > lines[j][1]:
            DP[i] = max(DP[i], DP[j] + 1)
print(N - max(DP))