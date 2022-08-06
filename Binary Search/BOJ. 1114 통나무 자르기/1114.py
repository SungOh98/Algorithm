'''
통나무 자르기
통나무를 여러개의 조각으로 나누려고 한다.
통나무의 길이는 L이고 k개의 위치에서만 자를 수 있다. 이 위치는 왼쪽으로부터 떨어진 거리이다.
통나무를 자를 수 있는 횟수는 최대 C번이다.
통나무의 가장 긴 조각을 최소로 만들고 그 길이와 그때 처음 잘랐던 위치를 출력하자
만약 가능한 것이 여러가지라면 처음 자르는 위치가 제일 작은 것을 출력하자.


임의의 길이 X이상으로 통나무를 자를 수 있는가?
있다면 X를 줄이기
없다면 X를 늘리기

O(N log L) 알고리즘 설계가 필요

임의의 길이 X가 주어졌을 때
모든 통나무의 길이를 X이하로 맟출 수 있는지에 대한 함수를 O(N)으로 설게해야함.

20% 중반 오답
반례
10 4 2
1 4 5 10

ans: 5 1

34% 오답임.
반례
9 8 2
1 2 3 5 6 7 8 9
'''


# O(N)으로 임의의 X이하로 통나무조각의 길이들을 맞출 수 있는지 판단하는 함수

def is_possible(arr, x, count):
    start, end = 0, 0

    while end < len(arr) and count > 0:
        while end < len(arr) and arr[end] - arr[start] <= x:
            end += 1

        if end >= len(arr):
            break

        count -= 1
        start = end - 1

    return l - arr[start] <= x, count

# pos는 pos길이 이하들로 통나무 조각들을 만들 수 있는 최소길이임.
def find_first_cut(pos, arr, count, c):
    if count > 0:
        return arr[1]
    # 역순으로 찾아야 한다.
    end = arr[-1]
    for i in range(len(arr) - 1, -1, -1):
        if end - arr[i] > pos:
            end = arr[i + 1]
            c -= 1
    return end



def parametric_search(arr, c):
    start, end = 1, l
    count = -1
    while start < end:
        mid = (start + end) // 2
        check, cnt = is_possible(arr, mid, c)
        if check:
            end = mid
            count = cnt
        else:
            start = mid + 1

    return f"{(start + end) // 2} {find_first_cut((start + end) // 2, arr, count, c)}"

l, k, c = map(int, input().split())
array = sorted(set([0] + [l] + list(map(int, input().split()))))

# print(get_first_cut(array, 1, c))
print(parametric_search(array, c))