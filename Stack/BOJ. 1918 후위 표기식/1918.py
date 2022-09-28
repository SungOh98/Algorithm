dic = {'(': 0, '+': 1, "-": 1, '*': 2, "/": 2}

'''
알고리즘
문자를 하나씩 살펴보며 다음과 같은 동작을 수행
1. 문자를 만날 경우 정답문자열에 붙임.
2. (를 만날 경우 무조건 스택에 삽입
3. 연산자를 만날 경우 스택에서 현재 확인하고 있던 연산자 보다 우선순위가 크거나 같은 연산자를 모두 정답 문자열에 붙이고 현재 검사하고 있던 연산자를 스택에 삽입
4. )를 만날 경우 (을 스택에서 꺼낼 때까지 스택에서 꺼낸 연산자를 정답연산자에 붙임.
5. 마지막으로 스택이 빌때 까지 스택에 남은 연산자들을 정답 문자열에 붙임 
'''
def Post(str, priority):
    stack = []
    answer = ''
    for obj in str:
        # 스택 삽입부
        if obj in '+-/*':
            # 스택이 비어있다면
            if not stack:
                stack.append(obj)
            # 스택이 비어있지 않다면
            else:
                while stack:
                    tmp = stack.pop()
                    # 새로 꺼낸 것이 우선순위가 obj보다 크거나 같다면
                    if priority[tmp] >= priority[obj]:
                        answer += tmp
                    # 새로 꺼낸 것의 우선순위가 obj보다 작다면
                    else:
                        stack.append(tmp)
                        break
                stack.append(obj)
        elif obj == "(":
            stack.append(obj)
        # 꺼낸 원소가 ")" 이거나 문자열이라면
        else:
            # 원소가 ")"라면
            if obj == ")":
                while stack:
                    tmp = stack.pop()
                    if tmp == "(":
                        break
                    answer += tmp
            # 원소가 문자열이라면
            else:
                answer += obj
    while stack:
        answer += stack.pop()
    return answer

str = input()
print(Post(str, dic))
'''
(x + y) - ( w * z ) / v
xy+wz*v/-

[(, +] : xy
[] : xy +
[-, (, *] : xy + wz
[-] : xy + wz *
[- /] : xy + wz * v
[] : xy + wz * v / -

( x * ( ( y + z ) - w ) + v )
[(] : x
[ (, * , (, (, +]: xyz
[ (, *, (] : xyz+
[(, *, (, -] : xyz+w
[(, * ] : xyz+w-
[(, + ] : xyz + w - * v
[] : xyz + w - * v +



'''