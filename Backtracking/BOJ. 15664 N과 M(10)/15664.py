'''
중복 되는 자연수가 있는 n개의 자연수들 중 m개를 고른 수열을 출력하시오
단 비내림차순이어야 하며, 중복된 수열을 출력하면 안된다.

4 2
1 7 9 9

1 7
1 9
1 9 (안됨)
7 9
7 9 (안됨)
9 9
'''

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))


def Backtracking(arr, idx, depth, ans):
    if depth >= m:
        print(ans)
        return

    prev = -1

    for i in range(idx, len(arr)):
        # ans 값이 이전 값과 중복되지 않다면 branch!
        if prev != ans + str(arr[i]) + ' ':
            Backtracking(arr, i + 1, depth + 1, ans + str(arr[i]) + ' ')
            # backtrack시 prev 설정
            prev = ans + str(arr[i]) + ' '
Backtracking(array, 0, 0, '')

