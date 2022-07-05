'''
n개의 자연수 중 m개를 고른 수열을 출력하시오
단 같은 수를 여러번 골라도 되고, 고른 수열은 비 내림 차순이여야 한다.
4 2
1 7 8 9

1 1
1 7
1 8
1 9
7 7
7 8
7 9
8 8
8 9
9 9
'''

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

def Backtracking(arr, idx, depth, ans):
    if depth >= m:
        print(ans)
        return

    for i in range(idx, len(arr)):
        Backtracking(arr, i, depth + 1, ans + str(arr[i]) + ' ')
Backtracking(array, 0, 0, '')