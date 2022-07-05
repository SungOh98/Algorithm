'''
n개의 자연수 중 m개를 고른 수열을 출력하시오, 단 중복된 숫자를 골라도 된다.
중복 순열 문제
출력 량이 많으므로 stdout 을 활용하여 시간을 단축하자.

4 2
1 7 8 9

1 1
1 7
1 8
1 9
7 1
7 7
7 8
7 9
8 1
8 7
8 8
8 9
9 1
9 7
9 8
9 9
'''
import sys
print = sys.stdout.write
n, m = map(int, input().split())
array = sorted(list(map(int, input().split())))

def Backtracking(arr, depth, ans):
    if depth >= m:
        print("%s\n" %ans)
        return

    for i in range(len(arr)):
        Backtracking(arr, depth + 1, ans + str(arr[i]) + " ")

Backtracking(array, 0, '')