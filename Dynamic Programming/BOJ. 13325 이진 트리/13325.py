h = int(input())
graph = [0, 0] + list(map(int, input().split()))
ans = sum(graph)
def dfs(node, depth, plus):
    global ans
    graph[node] += plus
    # 리프 노드일 경우
    if depth == h:
        return graph[node]
    # 리프 노드가 아닐 경우
    else:
        left = node * 2
        right = node * 2 + 1
        left_max = dfs(left, depth + 1, graph[node])
        right_max = dfs(right, depth + 1, graph[node])
        cur = max(right_max, left_max) - min(right_max, left_max)
        ans += cur
        return max(right_max, left_max)

dfs(1, 0, graph[1])
print(ans)