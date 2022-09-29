'''
구간합을 구할 배열을 구간배열이라고 부르자.
세그먼트 트리는 Full Binary Tree임.
세그먼트 트리는 구간합을 빠르게 구하기 위한 자료구조임.
세그먼트 트리의 리프노드에는 구간배열의 값 그 자체를 왼쪽 리프노드부터 채우고
세그먼트 트리의 리프노드가 아닌 노드에는 왼쪽 자식 노드와 오른쪽 자식 노드의 합을 저장한다.
세그먼트 트리는 기존의 구간배열과 별개로 트리 자료구조를 표현하기 위한 배열을 만든다.
-> 배열은 세그먼트 트리가 포화 이진 트리라고 가정하고 구현한다!  -> 리프 노드간의 깊이 차이가 별로 없어서 공간 낭비 적음
세그먼트 트리는 full binary Tree 이므로 다음과 같이 배열로 트리를 표현할 수 있다.
-> 어떤 노드를 arr[x]라고 하면
-> 어떤 노드의 왼쪽 자식 노드를 나타내는 인덱스는 2x이다.
-> 어떤 노드의 오른쪽 자식 노드를 나타내는 인덱스는 2x + 1이다.
세그먼트 트리 배열의 크기는 2^(H + 1) - 1이다. (H: 포화이진트리의 리프노드 개수)

'''

'''
기준 배열 기준으로 세그먼트 트리 배열의 틀을 생성해주는 함수
arr는 세그먼트 트리의 리프노드가 담긴 배열이다.
리프노드의 개수를 통해 포화이진트리를 표현할 배열의 크기를 결정해주는 함수
'''


def make_frame(array):
    H = 0
    leaf_num = 1  # 2^0
    while leaf_num < len(array):
        H += 1
        leaf_num *= 2
    return [-1] * (2 ** (H + 1))


# 2 ** H: 포화이진트리의 리프노드 개수
# 2 ** (H + 1) - 1 : 포화 이진트리의 총 노드 개수

'''
세그먼트 트리 배열 틀에 구간합을 저장해주는 함수
idx : 세그먼트 트리 배열에 접근하기 위한 인덱스 변수
start, end : 기준배열에 접근하기 위한 인덱스 변수
'''


def interval_sum(start, end, segment, idx):
    if start == end:
        segment[idx] = arr[start]
        return segment[idx]
    mid = (start + end) // 2
    segment[idx] = interval_sum(start, mid, segment, 2 * idx) + interval_sum(mid + 1, end, segment, 2 * idx + 1)
    return segment[idx]


def findIntervalSum(left, right, start, end, segment, idx):
    # 1번 조건
    if end < left or right < start:
        return 0
    # 2번 조건
    elif left <= start and end <= right:
        return segment[idx]
    # 3번 또는 4번 조건
    else:
        mid = (start + end) // 2
        return findIntervalSum(left, right, start, mid, segment, 2 * idx) \
                       + findIntervalSum(left, right, mid + 1, end, segment, 2 * idx + 1)



def update(diff, start, end, segment, k, idx):
    if start > k or end < k:
        return
    if start >= end:
        segment[idx] += diff
        return

    mid = (start + end) // 2
    update(diff, start, mid, segment, k, idx * 2)
    update(diff, mid + 1, end, segment, k, idx * 2 + 1)
    segment[idx] += diff
    return

def update_tree(k, value, arr, segment):
    diff = value - arr[k]
    arr[k] = value
    update(diff, 0, len(arr) - 1, segment, k, 1)

def change(value, start, end, idx, segment, k):
    # k가 현재 노드 범위에 없을 경우 -> 변경없이 해당 노드의 값 리턴
    if start > k or end < k:
        return segment[idx]
    # 리프노드를 만날 경우
    if start == end:
        segment[idx] = value
        return value

    mid = (start + end) // 2
    segment[idx] = change(value, start, mid, idx * 2, segment, k) + change(value, mid + 1, end, idx * 2 + 1, segment, k)
    return segment[idx]





# interval_sum(0, len(arr) - 1, ST, 1)
# print(ST)
arr = [5, 8, 7, 3, 2, 5, 1, 8, 9, 8, 7, 3]
ST = make_frame(arr)
interval_sum(0, len(arr) - 1, ST, 1)
print(findIntervalSum(3, 6, 0, len(arr) - 1, ST, 1))
