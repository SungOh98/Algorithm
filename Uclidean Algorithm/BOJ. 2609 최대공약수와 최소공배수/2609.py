'''
유클리드 호제법
1. 큰수를 작은 수로 나눈다.
2. 나눈 수를 나머지로 계속 나눈다.
3. 나머지가 0이라면 나눈 수가 최대 공약수이다.
Great Common Factor
Least Common Multiple
'''


def GCD(large, small):
    # base condition
    if small == 0:
        return large

    return GCD(small, large % small)


a, b = map(int, input().split())
gcd = GCD(a, b) if a > b else GCD(b, a)
lcm = (a // gcd) * (b // gcd) * gcd
print(gcd)
print(lcm)
