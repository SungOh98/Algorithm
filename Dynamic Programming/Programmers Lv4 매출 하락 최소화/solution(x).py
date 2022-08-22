'''
2 <= N <= 300,000 개의 노드의 트리
각 노드마다 노드 번호, 매출량이 주어짐

각 노드는 세가지 경우의 수가 존재
팀장이면서 팀원 일 수 있다.
팀원일 수 있다.
팀장일 수 있다.

모든 팀에서 최소 1명이상 워크숍에 참석 시켜야 한다.
하지만 매출하락 최소화를 위해 워크숍에 참석하는 직원들의 매출액의 이 최소가 되어야 한다.

한팀은 무조건 팀장과 팀원으로 이루어져야 한다.
하나의 노드만으로는 팀을 구성할 수 없다.

i번 노드까지의 드는 비용의 최소값.
dp[0][i]는 i번 노드를 선택했을 경우에 대한 i번 노드까지의 최소값
>> i번 노드를 선택했으므로 i번 노드의 자식 노드 중 필수로 선택해야하는 자식만 더 선택해주면 된다.
dp[1][i]는 i번 노드를 선택하지 않았을 경우에 대한 i번 노드까지의 최소값
>> i번 노드를 선택하지 않았으므로 i번 노드의 자식 노드 중 하나를 필수로 선택해야 한다.
따라서 여러가지 경우의 수가 생기게 된다.
'''


def dfs(tree, node, choice, sales):
    sel, rej = float('inf'), float('inf')
    for child in tree[node]:
        c_sel, c_rej = dfs(tree, child, True, sales), dfs(tree, child, False, sales)

        if choice:
            sel = min(sel, min(c_sel, c_rej))


    # 리프 노드일 경우
    if sel == float('inf'):
        if choice:
            return sales[node]
        else:
            return 0




def make_tree(sales, edges):
    N = len(sales)
    tree = [[] for _ in range(N)]
    for a, b in edges:
        tree[a].append(b)

    return tree


def solution(sales, links):
    tree = make_tree([0] + sales, links)
    answer = 0

    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
               [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
