'''
k번째 수
NxN 배열 A[i][j]  = i X j 이다.
이 배열의 요소를 일차원 배열 B에 넣고 정렬한 후
B[k] 를 구해보자.

B와 A의 인덱스는 1부터 시작한다.

입력 크기가 최대 100,000 이므로
O(N log N) 의 알고리즘 설계가 필요하다.

노션에 풀이 적음

'''


def count_of_smaller(x):
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, x // i)

    return cnt


def parametric_Seach():
    start, end = 1, 1_000_000_000

    while start < end:
        mid = (start + end) // 2

        i = count_of_smaller(mid)

        if i >= k:
            end = mid

        else:
            start = mid + 1

    return (start + end) // 2


n = int(input())
k = int(input())
# print(count_of_smaller(7))
print(parametric_Seach())