import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline


def Depth_First_Search(parent, depth, start, depth_arr):
    depth_arr[start] = depth

    for node in graph[start]:
        if depth_arr[node] == -1:
            Depth_First_Search(parent, depth + 1, node, depth_arr)

            # backtrack시 바로 위의 부모 정보를 0번째에 저장.
            parent[node][0] = start


'''
2 = 1 + 1
4 = 2 + 2
8 = 4 + 4
...

해당 노드의 4번째 위의 부모는 2번째 위의 부모의 2번째 위의 부모이다.
해당 노드의 8번째 위의 부모는 4번째 위의 부모의 4번째 위의 부모이다.
>> 재귀적 관계식! 
'''


def Dynamic_Programming(parent):
    # 2^i번쨰 부모
    for i in range(1, 18):
        for node in range(1, n + 1):
            parent[node][i] = parent[parent[node][i - 1]][i - 1]

    return parent


def LCA(a, b, parent, depth_arr):
    # 먼저 높이를 맞추기.
    min_depth = min(depth_arr[a], depth_arr[b])

    while depth_arr[a] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parent[a][i]] >= min_depth:
                a = parent[a][i]
                break
    while depth_arr[b] > min_depth:
        for i in range(17, -1, -1):
            if depth_arr[parent[b][i]] >= min_depth:
                b = parent[b][i]
                break

    # 점프
    # 바로 위의 부모가 같으면 중지
    while parent[a][0] != parent[b][0]:
        for i in range(17, -1, -1):
            if parent[a][i] != parent[b][i]:
                a, b = parent[a][i], parent[b][i]
                break

    if a == b:
        return a
    else:
        return parent[a][0]




def main_func():
    # 각 노드 별(행) 2^i 번째 부모들을 기록할 부모 테이블!
    # 최악의 경우 log 100000 < 17 개의 부모들을 저장.
    parent = [[0] * 18 for _ in range(n + 1)]
    depth_arr = [-1] * (n + 1)
    Depth_First_Search(parent, 0, 1, depth_arr)
    parent = Dynamic_Programming(parent)
    for a, b in nodes:
        print(LCA(a, b, parent, depth_arr))



n = int(input())
graph = [[] for _ in range(n + 1)]


for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

nodes = []
m = int(input())
for _ in range(m):
    nodes.append(tuple(map(int, input().split())))

# Depth_First_Search(parent, 0, 1, [-1] * (n + 1))
# parent = Dynamic_Programming(parent)
# for i in parent:
#     print(i)
main_func()