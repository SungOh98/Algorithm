"""
중복된 수가 포함된 n개의 자연수 중 m개를 고른 수열을 출력하시오
단 같은 수를 여러번 골라도 되며, 중복되는 수열을 여러번 출력하면 안된다.

4 2
1 7 9 9

1 1
1 7
1 9
1 9(안됨)
7 1
7 7
7 9
7 9(안됨)
9 1
9 7
9 9
9 9(안됨)
9 1(안됨)
9 7(안됨)
9 9(안됨)
9 9(안됨)

"""



n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))


def Backtracking(arr, depth, ans):
    if depth >= m:
        print(ans)
        return

    prev = -1

    for i in range(len(arr)):
        # ans 값이 이전 값과 중복되지 않다면 branch!
        if prev != ans + str(arr[i]) + ' ':
            Backtracking(arr, depth + 1, ans + str(arr[i]) + ' ')
            # backtrack시 prev 설정
            prev = ans + str(arr[i]) + ' '
Backtracking(array, 0, '')

