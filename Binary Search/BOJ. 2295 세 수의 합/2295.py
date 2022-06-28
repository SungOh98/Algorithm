'''
�� ���� ��
n���� �ڿ������ �̷���� ���� s�� �ִ�.
�� �߿��� �� ���� ���� �� ������ ���� ������ ���� s�� �ִ� ��찡 �ִ�.
�̷� ���� �� ���� ū ������ �� d�� ã����.
�Է����� �޴� ������ ��� �ٸ� ���ڵ� �̴�.
������ ���Ƶ� �ȴ�.
5 <= N <= 1000
baaaaaaking dog���� ���� ���� Ǯ��

arr[i], arr[j], arr[k] �� ���� ã�� ��������
arr[i]�� arr[j]�� ���� �̸� ������ ���� temp �迭�� �����
temp ���� �̺� Ž���� �����Ͽ� arr[l] - arr[k] ���� �ִ��� �����ϴ� ���� �ٽ� ���̵��
( arr[k] + temp[i] �� arr�� ������ �ϳ��� �ִٸ� �����̹Ƿ�! )
'''
# �ΰ��� �̸� ���� ���� �迭�� ����
def make_new_arr(arr):
    temp = set()
    for i in range(n):
        for j in range(i, n):
            temp.add(arr[i] + arr[j])
    temp = sorted(temp)
    return temp

def binary_search(array, start, end, target):
    if start > end:
        return False

    mid = (start + end) // 2

    if array[mid] == target:
        return True

    elif array[mid] > target:
        return binary_search(array, start, mid - 1, target)

    else:
        return binary_search(array, mid + 1, end, target)


def main_func():
    # n^2
    new_arr = make_new_arr(arr)
    # n^2
    for i in range(n - 1, -1, -1):
        for j in range(n):
            # logn
            if binary_search(new_arr, 0, len(new_arr) - 1, arr[i] - arr[j]):
                return arr[i]
    # total = O{(n^2) log n}
import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(main_func())