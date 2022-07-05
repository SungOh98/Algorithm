'''
n과 m이 주어질 때
n개의 자연수 중 m개를 고른 수열을 구하시오 (오름 차순)

예
4 2
9 8 7 1

1 7
1 8
1 9
7 8
7 9
8 9

combination문제임.
'''

n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

def Combination(arr, idx, depth, ans):
    if depth >= m:
        print(ans)
        return

    for i in range(idx, len(arr)):
        Combination(arr, i + 1, depth + 1, ans + "{} ".format(arr[i]))
Combination(array, 0, 0, '')