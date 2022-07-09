'''
국가의 예산을 지방 예산 요청에 따라 분배를 해야한다.
정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 분배하려고 한다.
1. 모든 요청이 배정될 수 있는 경우, 요청한 금액 그대로 배정한다.
2. 그럴 수 없는 경우, 특정한 정수 상한액을 정하여 그 이상인 요청들에 대해서는 모두 상한액을 배정한다.
상한액 이의 예산 요청일 경우 요청한 금액을 배정한다.

최대 최소 문제이면서 입력값이 크다 >> 파라메트릭 서치를 의심해보자

1. 결정문제로 바꿀 수 있는가?
임의의 상한 배정액에 대해 각 지역에 모두 분배할 수 있는가? 아닌가?

2. 상한 배정액이 증가/ 감소 함수의 형태로 결정되는가? 증가!

'''

def check(arr, have):
    total = 0
    max_m = 0

    for i in arr:
        max_m = max(max_m, i)
        total += i

    if total <= have:
        return max_m
    else:
        return 0


def get_sum(arr, top):
    money = 0
    for i in range(len(arr)):
        if arr[i] > top:
            money += top
        else:
            money += arr[i]

    return money


def binary_search(arr, total_money):
    start, end = 0, 1000000000
    # log(10억)
    while start <= end:
        top_boundary = (start + end) // 2
        # n
        alloc_money = get_sum(arr, top_boundary)

        # 요청 예산이 국가 예산 보다 클 경우
        if alloc_money > total_money:
            end = top_boundary - 1

        # 요청 예산이 국가 예산 보다 작거나 같을 경우
        else:
            start = top_boundary + 1

    return (start + end) // 2

def main_func():
    possible = check(array, total)
    # n
    if possible:
        return possible
    else:
        # nlog(10억)
        return binary_search(array, total)

n = int(input())
array = list(map(int, input().split()))
total = int(input())
# print(binary_search(array, total))
print(main_func())
