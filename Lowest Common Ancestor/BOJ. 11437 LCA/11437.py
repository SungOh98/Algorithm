'''

최소 공통 조상 구하는 알고리즘.
1. 그래프 탐색 알고리즘을 통해 각 노드에 대한 깊이를 저장하는 배열과 부모노드의 정보를 저장하는 배열을 만든다.
2. 조사할 두 노드의 깊이를 맞춘다.
3. 두 노드가 같아질때까지 번갈아가며 낮은 높이의 노드로 올라간다.

모든 노드들에 대하여 부모 노드를 기록하여
해당 노드에서 부모 노드로 향할 때 theta(1)의 시간을 보장할 수 있게끔 한다.

한쪽으로 치우친 트리가 입력으로 주어졌을 때가 최악의 경우
O(MN)을 보장하는 알고리즘.
'''

# 깊이 우선 탐색으로 깊이를 저장할 배열 만들어주기.
# theta(n + n - 1)
def depth_first_search(depth, depth_arr, start, parent):
    depth_arr[start] = depth

    for node in graph[start]:
        if depth_arr[node] == -1:
            depth_first_search(depth + 1, depth_arr, node, parent)

            # backtrack 시 부모 정보를 Memoization
            parent[node] = start


def Lowest_Common_Ancestor(a, b, depth_arr, parent):

    # 먼저 깊이 맞추어주기
    min_depth = min(depth_arr[a], depth_arr[b])

    while depth_arr[a] > min_depth:
        a = parent[a]

    while depth_arr[b] > min_depth:
        b = parent[b]
        '''
        부모 노드를 메모하지 않았다면 다음과 같이 매번 간선을 확인하며 올라가야함 >> 비효율적
        for node in graph[b]:
            if depth_arr[node] < depth_arr[b]:
                b = node
                break
        '''

    # 두 노드가 같아질 때까지 번갈아가며 올라가기

    while a != b:
        a = parent[a]
        b = parent[b]

    return a





def main_func():
    depth_arr = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    depth_first_search(0, depth_arr, 1, parent)
    for a, b in nodes:
        print(Lowest_Common_Ancestor(a, b, depth_arr, parent))



import sys
sys.setrecursionlimit(50001)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
# depth_arr = [-1] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

nodes = []
m = int(input())
for _ in range(m):
    nodes.append(tuple(map(int, input().split())))

main_func()