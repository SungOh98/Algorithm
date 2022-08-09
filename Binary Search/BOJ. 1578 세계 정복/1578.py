'''
N개의 국가가 있다.
각국가당 사람수도 주어진다,
세준이는 모든 사람들을 다음 규칙에 맞게 최대 몇 그룹으로 나눌 수 있는지 궁금해졌다.
1. 그룹에 들어있는 사람 수는 정확히 K명
2. 그룹에 속한 사람들은 모두 다른 나라 사람이여야한다.
남는 사람은 무시해도 된다.

1 <= K <= 20
K <= N <= 50
1 <= 국가별 사람 수 <= 1_000_000_000

파라메트릭 서치
최적화: 그룹의 최대 개수를 구하여라
결정: 그룹의 개수가 임의의 X일 때 그룹을 나눌 수 있는가?
있다면 >> 늘리기
없다면 >> 줄이기.

결정함수
하나의 국가 출신의 사람은 하나의 그룹에 두 명 이상 들어갈 수 없다.
- 그룹의 수는 매우 많을 수 있으므로 그룹을 모두 탐색하는 것은 무리
- 사람수도 매우 많으므로 사람 한명씩 분배하는 것도 무리
>> 수식으로 풀어야함.
'''


def is_possible(arr, x, k):
    # 임의의 그룹 수보다 사람 수가 적은 국가들은 모두 합해주기
    lower_sum = 0
    # 임의의 그룹 수보다 사람 수가 많은 국가의 개수를 세주기 >> 그룹당 한명씩 채운 것(나머지는 버릴 수 밖에 없음)
    higher_cnt = 0

    for i in arr:
        if i >= x:
            higher_cnt += 1
        else:
            lower_sum += i


    return (higher_cnt + (lower_sum // x)) >= k


def parametric_search():
    start, end = 0, 2 ** 63 - 1
    while start <= end:
        mid = (start + end) // 2
        if is_possible(array, mid, k):
            start = mid + 1
        else:
            end = mid - 1

    return (start + end) // 2


n, k = map(int, input().split())
array = list(map(int, input().split()))
# print(array)
print(parametric_search())
