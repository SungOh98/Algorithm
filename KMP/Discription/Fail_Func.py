'''
실패 함수 F(x) = 문자열 S[0:x + 1] 에서 접두사와 접미사가 일치하는 최대 길이.

'''

# O(|s| ^ 2) fail Func
# s: 문자열
def fail_func(s, x):
    # O(x)
    tmp = s[:x + 1]
    #F(x)의 값이 x, x - 1, x - 2 ... 0인지 판단
    for ans in range(x, 0, -1):
        flag = True
        inter = len(tmp) - ans
        for i in range(ans):
            if tmp[i] != tmp[inter + i]:
                flag = False
                break
        if flag:
            return ans

    return 0
# 하나의 X에 대한 fail_func -> O(s^2)
# 전체 X에 대한 fail_func -> O(S^3)
s = "ABABCABABA"
print(fail_func(s, 9))