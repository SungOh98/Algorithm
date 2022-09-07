'''
함수 정의
func(n, r, c): 2^n * 2^n 배열에서 (r, c)를 방문하는 순서를 반환하는 함수
base condition
n = 0 일때 return 0
재귀식
(r, c)가 1번 사각형일 때 return func(n - 1, r, c)
(r, c)가 2번 사각형일 때 return half*half + func(n - 1, r, c - half)
(r, c)가 1번 사각형일 때 return 2*half*half + func(n - 1, r - half, c)
(r, c)가 1번 사각형일 때 return 3*half*half + func(n - 1, r - half, c - half)

'''


def divide_and_conquer(n, r, c):
    if n == 0:
        return 0
    half = 1 << (n - 1)
    if (r < half and c < half):
        return divide_and_conquer(n - 1, r, c)
    elif (r < half and c >= half):
        return half * half + divide_and_conquer(n - 1, r, c - half)
    elif (r >= half and c < half):
        return 2 * half * half + divide_and_conquer(n - 1, r - half, c)
    else:
        return 3 * half * half + divide_and_conquer(n - 1, r - half, c - half)


N, row, col = map(int, input().split())
print(divide_and_conquer(N, row, col))
