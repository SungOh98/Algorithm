'''
1. 받은 문자열을 하나씩 순회하며 다음과 같은 과정을 반복한다.
2. 연산자가 나올 때까지 숫자를 스택에 삽입한다.
3. 연산자가 나올 경우 스택의 최상단 원소 2개를 꺼낸 후 연산한다. 그 후 연산값을 스택에 다시 삽입한다.
'''

values = {}
stack = []
operator = "*+-/"
n = int(input())
equation = input()
for i in range(65, 65 + n):
    values[chr(i)] = int(input())
for ch in equation:
    if ch in operator:
        second, first = stack.pop(), stack.pop()
        if ch == "*":
            stack.append(first * second)
        elif ch == "+":
            stack.append(first + second)
        elif ch == "/":
            stack.append(first / second)
        elif ch == "-":
            stack.append(first - second)
    else:
        stack.append(values[ch])
print(f"{stack[0]:.2f}")


