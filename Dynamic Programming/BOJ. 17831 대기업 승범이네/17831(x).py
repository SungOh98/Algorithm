'''
한 직원이 멘토임과 동시에 멘티일 수는 없다.
한 직원이 여러명의 멘토일 수 없다.

'''

def dfs(node, synergy, dp):

    m, nm = 0, 0
    for child in graph[node]:
        cm, cnm = dfs(child, synergy, dp)
        syn = synergy[child] * synergy[node]
        m = max(cnm + syn, nm + max(cm, cnm))
        nm += max(cm, cnm)


    if graph[node] == []:
        return 0, 0

    return m, nm


n = int(input())
parents = [0, 0] + list(map(int, input().split()))
synergy = [0] + list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[parents[i]].append(i)
print(graph)