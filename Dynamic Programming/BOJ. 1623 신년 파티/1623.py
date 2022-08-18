'''
메모리 초과....
'''

def dfs(graph, node, array):

    p_include, p_exclude = array[node], 0
    path_include, path_exclude = [node], []
    for child in graph[node]:

        c_include, c_exclude, c_path, c_path2 = dfs(graph, child, array)
        p_include += c_exclude
        path_include += c_path2

        if c_include > c_exclude:
            p_exclude += c_include
            path_exclude += c_path
        else:
            p_exclude += c_exclude
            path_exclude += c_path2


    return p_include, p_exclude, path_include, path_exclude


import sys
sys.setrecursionlimit(200001)
input = sys.stdin.readline
n = int(input())
weights = [0] + list(map(int, input().split()))
parents = [0, 0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    graph[parents[i]].append(i)
a, b, c, d = dfs(graph, 1, weights)
print(a, b)
for i in sorted(c):
    print(i, end=" ")
print(-1)
for i in sorted(d):
    print(i, end=" ")
print(-1)