'''
레이스
길이 N의 트랙에
심판 M명을 K곳에 설치하려고 한다.
가장 가까운 두 심판의 거리의 최대값을 구하자.
1 <= N <= 1,000,000
2 <= K <= 50
M <= K

임의의 거리 X만큼 떨어뜨려 심판을 배치시킬 수 있는가?
있다면 >> 거리 늘리기
없다면 >> 거리 줄이기.
반례
11 3 4
0 3 8 11

ans: 1110
'''

def possible(arr, x, m):
    start, end = 0, 0

    ans = ["0"] * len(arr)

    while start < len(arr):
        # arr[end] 에 심판 한명 두기
        m -= 1
        ans[end] = "1"
        if m <= 0:
            break
        # 임의의 X 거리를 두고 다음 심판을 둘 end 찾기
        while end < len(arr) and arr[end] - arr[start] < x:
            end += 1
        start = end
    return m <= 0, "".join(ans)

def parametric_search():
    start, end = 1, 1000000
    answer = ""
    while start <= end:
        mid = (start + end) // 2
        flag, tmp = possible(array, mid, m)

        if flag:
            start = mid + 1
            answer = tmp

        else:
            end = mid - 1

    return answer


n, m, k = map(int, input().split())
array = list(map(int, input().split()))
# print(possible(array, 5, m))
print(parametric_search())