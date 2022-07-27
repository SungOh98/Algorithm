'''
<서론>
블루레이는 총 N개의 강의가 들어가는데 , 블루레이를 녹화할 때 강의의 순서가 바뀌면 안된다.
즉 i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j사이의 모든 강의도 블루레이에 녹화 해야한다.

<본론>
강토는 M개의 블루레이에 모든 강의 동영상을 녹화하려고 한다.
이때 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 또한 M개의 블루레이는 모두 같은 크기여야 한다.
강의의 수 N 과 블루레이의 수 M이 주어질때 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.


<Parametric Search Problem>
1. 최적화 문제를 결정문제로 바꿀 수 있는가?
최적화: 가능한 블루레이 크기 중 최소를 구하자 -> 결정 임의의 블루레이 크기 X에 대해 모든 강의를 담을 수 있는가?
>> 담을 수 있다면 블루레이 크기를 줄임 >> end = mid 로 바꾸어 다음 mid의 값을 줄임
>> 담을 수 없다면 블루레이 크기를 늘림 >> start = mid + 1 로 바꾸어 다음 mid의 값을 늘림.
2. 매개변수 X가 증가 또는 감소함수 형태인가? OKAY

추가로 강의 순서가 바뀌면 안되므로 정렬은 필요없다.

틀렸던 이유: 블루레이 크기는 10000이 최대가 아니다
100000개의 강의와 모든 강의의 시간이 10000이며, 블루레이 수는 1개라면
100000 * 10000인 10억 이 답이 될 수 있다.
'''

def is_possible(arr, x, m):
    if max_v > x:
        return False

    idx = 0
    sum = 0
    while idx < n and m > 0:

        m -= 1
        sum = arr[idx]

        while idx < n and sum <= x:
            idx += 1

            if idx >= n:
                break
            sum += arr[idx]

        if idx < n - 1 and m <= 0:
            return False


    return sum <= x


def parametric_search(arr, m):
    start, end = 0, 1_000_000_000

    while start < end:

        parameter = (start + end) // 2

        if is_possible(arr, parameter, m):
            end = parameter
        else:
            start = parameter + 1

    return (start + end) // 2


n, m = map(int, input().split())
array = list(map(int, input().split()))
max_v = max(array)
print(parametric_search(array, m))
# print(is_possible(array, 23, m))