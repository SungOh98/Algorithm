'''
트리의 높이와 너비
이진 트리를 다음 규칙에 따라 행과 열의 번호가 붙어 있는 격자 모양의 틀속에 그림
1. 이진 트리에서 같은 레벨에 있는 노드는 같은 행에 위치
2, 한 열에는 한 노드만 존재
3. 임의의 노드의 왼쪽 서브트리에 있는 노드들은 해당 노드보다 왼쪽의 열에 위치
오른쪽 서브트리에 있는 노드들은 해당 노드보다 오른쪽의 열에 위치
4. 노드가 배치된 가장 왼쪽 열과 오른쪽 열 사이엔 아무 노드도 없이 비어 있는 열은 없다.

중위 순회하면서 붙이면 될 듯.

트리를 어떻게 표현할지가 문제임.
> 일단 인접 리스트로 해보자.

2차원 배열을 만들 경우 -> 한쪽으로 치우친 트리일 경우 시간초과 뜰 가능성이 있음.

루트 노드가 당연히 1인
'''
col = 0

# 중위 순회 함수,
def inorder(tree, level, node, width):
    global col
    # base Condition
    if node == -1:
        return

    left, right = tree[node]

    inorder(tree, level + 1, left, width)

    col += 1
    # 각 level 별 너비 갱신
    if width[level][0] > col:
        width[level][0] = col
    if width[level][1] < col:
        width[level][1] = col
    inorder(tree, level + 1, right, width)



'''
트리의 높이를 구해주는 함수
현재 노드를 루트로하는 서브트리의 높이: max(왼쪽 서브트리의 높이, 오른쪽 서브트리의 높이) + 1
내가 아는 작은 문제로 분해 -> 노드가 한개인 트리의 높이는 1임.
'''
def cal_height(tree, node):
    if node == -1:
        return 0
    left, right = tree[node]

    if left == -1 and right == -1:
        return 1

    return max(cal_height(tree, left), cal_height(tree, right)) + 1


def main_func(root):
    global col
    height = cal_height(tree, root)
    width = [[float('inf'), - 1] for _ in range(height + 1)]
    inorder(tree, 1, root, width)
    max_level = height
    max_width = -1
    for i in range(height, 0, -1):
        WIDTH = width[i][1] - width[i][0] + 1
        if WIDTH >= max_width:
            max_width = WIDTH
            max_level = i
    return f"{max_level} {max_width}"



import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [0 for i in range(n + 1)]
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a].append(b)
    tree[a].append(c)
    if b != -1:
        parents[b] = a
    if c != -1:
        parents[c] = a
root = 0
for i in range(1, n + 1):
    if parents[i] == 0:
        root = i

print(main_func(root))
