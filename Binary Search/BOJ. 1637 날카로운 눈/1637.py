'''
1 <= N <= 20,000 개의 정수 더미가 존재함
정수 더미에서는 하나의 숫자만 홀수개가 존재하고
나머지 수들은 모두 짝수개이다.

짝수의 합은 짝수이다.
2 + 2 = 4
4 + 12 = 14

홀수 + 짝수 = 홀수이다.

따라서 임의의 X까지의 X이하의 수들의 합이 홀수가 나온 경우 홀수가 포함된다는 것을 알 수 있다.
>> 파라메트릭 서치로 임의의 X를 정하고
X이하의 수의 개수의 합이 최초로 홀수가 나온 시점을 구하면 된다.

>> X이하의 개수의 합이 홀수가 나온다면 >> X를 낮게 조정
>> X이하의 개수의 합이 짝수가 나온다면 >> X를 크게 조정.

결정함수는 O(NlogN)로 N개의 정수 더미에서 X이하의 숫자들의 개수를 구할 수 있어야 한다.
'''

# 정수 더미들에서 임의의 X 이하의 정수들의 개수를 세는 func
# 각 정수 더미는 range(start, end, step) 형태로 주어진다.
def sum_is_odd(arr, x):
    _sum = 0
    for start, end, step in arr:
        if x >= end:
            _sum += (end - start) // step + 1
        elif start <= x:
            _sum += (x - start) // step + 1
    return _sum % 2 != 0

def get_count(number, arr):
    cnt = 0
    for start, end, step in arr:
        if start <= number <= end:
            if (number - start) % step == 0:
                cnt += 1
    return cnt

def parametric_search(arr):
    start, end = 1, 2 ** 31
    answer = 0
    while start < end:
        mid = (start + end) // 2

        if sum_is_odd(arr, mid):
            answer = mid
            end = mid

        else:
            start = mid + 1
    if (start + end) // 2 == 2 ** 31:
        return "NOTHING"
    else:
        return f"{answer} {get_count(answer, arr)}"

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

print(parametric_search(array))