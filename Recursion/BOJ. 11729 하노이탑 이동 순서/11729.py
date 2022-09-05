'''
N개의 원판을 A에서 C로 옮기려면
1. 어찌 됐던 N번 원판을 A에서 C로 옮겨야한다. >> N-1개의 원판을 원하는 곳으로 이동 시킬 수 있다면 된다.
2. 또한 1~N-1번 원판들은 B로 옮겨야 한다.
3. 그 후  1 ~ N-1번 원판들을 C로 옮긴다. >> N-1개의 원판을 원하는 곳으로 이동 시킬 수 있다면 된다.

핵심은 N-1개의 원판을 원하는 곳으로 이동 시킬 수 있느냐이다. > 사실관계를 기반으로 추론해보자.
>> N-1개의 원판을 원하는 곳으로 이동 시킬 수 있다면 N개의 원판을 원하는 곳으로 이동 시킬 수 있다.


1개의 원판은 원하는 대로 이동시킬 수 있다.
2개의 원판은 1개의 원판을 원하는 곳으로 이동시킬 수 있으므로 이동시킬 수 있다.
3개의 원판도 마찬가지.
.. N개의 원판도 마찬가지.
따라서 N개의 원판을 원하는 대로 이동시킬 수 있다.

사실 밑에 두개의 근거만으로도 귀납적 풀이가 가능하다는 것을 알아야함.
1. 원판이 1개라면 원하는 곳으로 이동시킬 수 있다.
2. 원판이 K-1개일때 원하는 곳으로 이동시킬 수 있다면 원판이 K개일때 원하는 곳으로 이동시킬 수 있다.
'''


# A = 1, B = 2, C = 3
# x도 y도 아닌 원판 >> 6 - x - y


def recur(n, start, end):
    if n == 1:  # base condition >> 여기로 수렴해야함.
        print(start, end)
        return
    else:
        recur(n - 1, start, 6 - start - end)  # N-1번 까지의 원판을 B로 옮긴다.
        print(start, end)  # N번 원판을 C로 옮긴다.
        recur(n - 1, 6 - start - end, end)  # N-1번 까지의 원판을 C로 옮긴다.

'''
T(N) = T(n - 1) + 1 + T(n - 1)
>> N개의 하노이 탑을 옮기기 위해서는 N - 1개를 옮기고, 1개를 옮기고 , N - 1개를 옮겨야함.
'''
n = int(input())
# 하노이 탑 이동 순서 시간 복잡도 O(2 ^ n)
print((1 << n) - 1)
recur(n, 1, 3)

