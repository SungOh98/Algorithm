# power 메소드는 수가 엄청 켜졌다가 종료하면서 작아짐 >> 결국 엄청 커지니 시간 많이듬
# O(logn)
def power(x, n):
    if n == 0:
        return 1

    else:
        if n % 2 == 0:
            return power(x * x, n // 2) % c
        else:
            return x * power(x * x, (n - 1) // 2) % c

# fpow 메소드는 그떄그때 나머지 연산을 취해주므로 수가 매우커지는 것을 방지한다. >> 따라서 매우 빠름.
# 나머지 분배법칙 : (A*B) % C = (A % C) * (B % C)
# (3^5) % 5 = (3 * fpow(3 * 3, 2)) % 5 = (3 % 5) * (fpow(3 * 3, 2) % 5)
# O(logn) + 큰 수 처리 overhead
def fpow(x, n):
    if n == 1:
        return x % c
    else:
        tmp = fpow(x, n // 2)
        if n % 2 == 0:
            return tmp * tmp % c
        else:
            return tmp * tmp * x % c
# 위 두 메소드 모두 O(logn)이다. 단지 수가 매우커지고 아니고에 따라 메모리 할당의 시간 차이이다.

def brute_force(x, n):
    mul = 1
    for _ in range(n):
        mul *= x
    return mul
# 너는 그냥 O(n) + 큰 수 처리 overhead

import time
import random

n, m, c = map(int, input().split())
s = time.time()
fpow(n, m)
e = time.time()
print(e - s)
s = time.time()
power(n, m)
e = time.time()
print(e - s)

