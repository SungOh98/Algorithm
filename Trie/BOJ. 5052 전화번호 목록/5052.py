'''
허프만 코드랑 비슷한듯.
인접 리스트로 트리를 만들게 되면 메모리 / 시간 초과임이 분명함.
링크를 가진 노드로 메모리를 절약하며 트리를 만들자.

각 노드당 10개의 링크와 데이터를 가지게 끔 해보자.
간선을 따라 트리를 만들며 이미 데이터가 존재하면 안됨 -> 완성된 번호는 무조건 리프노드에 존재해야함.
링크를 꼭 10개다 만들 필요가 있을 까?
1
3
91125426
911
97625999
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.links = [None] * 10

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, number):
        tmp = self.root
        for c in number:
            if tmp.data is not None:
                return 'NO'

            if tmp.links[int(c)] is None:
                tmp.links[int(c)] = Node(None)
            tmp = tmp.links[int(c)]
        tmp.data = number
        return 'YES'

import sys
input = sys.stdin.readline
TC = int(input().rstrip())
for _ in range(TC):
    n = int(input().rstrip())
    numbers = []
    for _ in range(n):
        numbers.append(input().rstrip())

    trie = Trie()
    flag = 'YES'
    # 짧은 애들 부터 해야함!!
    numbers.sort()
    for number in numbers:
        flag = trie.insert(number)
        if flag == 'NO':
            break
    print(flag)


