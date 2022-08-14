'''
반례
1
7
I 53
I 34
D -1
I -82
D 1
I 34
D 1
ans: -82 -82
'''
import heapq
from collections import defaultdict
import sys
def pop_min_heap():
    if length_of_pq > 0:
        while min_pq:
            number = heapq.heappop(min_pq)
            if min_dic[number] == 0:
                break
            else:
                min_dic[number] -= 1
        # max heap에서 사라진 원소를 표시해줌
        max_dic[number] += 1
        return True
    return False


def pop_max_heap():
    if length_of_pq > 0:
        while max_pq:
            number = -heapq.heappop(max_pq)
            if max_dic[number] == 0:
                break
            else:
                max_dic[number] -= 1
        # min heap에서 사라진 원소를 표시해줌
        min_dic[number] += 1
        return True
    return False

def insert(number):
    heapq.heappush(min_pq, number)
    heapq.heappush(max_pq, -number)


input = sys.stdin.readline
TC = int(input())
for _ in range(TC):
    # Priority Queue
    min_pq, max_pq = [], []
    # 삭제된 요소를 저장할 딕셔너리
    min_dic, max_dic = defaultdict(int), defaultdict(int)

    length_of_pq = 0

    n = int(input())

    for _ in range(n):
        order, num = input().split()
        if order == "I":
            insert(int(num))
            length_of_pq += 1

        else:
            if num == "-1":
                if pop_min_heap():
                    length_of_pq -= 1

            else:
                if pop_max_heap():
                    length_of_pq -= 1

    min_value, max_value = -1, -1
    answer = "EMPTY"
    if length_of_pq > 0:
        while True:
            min_value = heapq.heappop(min_pq)
            if min_dic[min_value] == 0:
                break
            else:
                min_dic[min_value] -= 1
        while True:
            max_value = -heapq.heappop(max_pq)
            if max_dic[max_value] == 0:
                break
            else:
                max_dic[max_value] -= 1
        answer = f"{max_value} {min_value}"

    print(answer)
