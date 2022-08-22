'''
내가 생각한 핵심: 중복된 시간을 뺴줘야 한다.
어떻게 중복된 시간을 확인할까?

'''

def dfs(graph, node):
    cur = []
    for child in graph[node]:
        cur += [dfs(graph, child)]

    # 리프 노드일 경우
    if not len(graph[node]):
        return 1

    # 자식노드 한 개 일 경우
    elif len(graph) == 1:
        return cur[0] + 1

    # 자식노드가 여러개 일 경우
    else:
        ans = 0
        cur.sort(reverse=True)
        start_time = 1
        for i in cur:
            ans = max(ans, start_time + i)
            start_time += 1
        return ans




n = int(input())
graph = [[] for _ in range(n)]
parent = list(map(int, input().split()))
for i in range(1, n):
    graph[parent[i]].append(i)
print(dfs(graph, 0) - 1)