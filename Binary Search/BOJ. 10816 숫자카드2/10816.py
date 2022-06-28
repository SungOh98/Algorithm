# ����ī�� 2
# ����̴� n���� ����ī�带 ������ �ִ�.
# ���� m���� �־����� ��, �� ���� �����ִ� ����ī�带 ����̴� ��� ������������
# ���� Ǯ�� >> �־��� ���
import sys

iput = sys.stdin.readline

n = int(input())
array = sorted(list(map(int, input().split())))
m = int(input())
things = list(map(int, input().split()))

# target�� ���� �������� ã�� ���� ���� Ž�� �Լ�
'''
������ ���� Ž���� ����
������ ���� Ž������ arr[mid] == target�̸� ����� return �ϴµ� �ݿ�
������ �κ��� arr[mid] == target�̶� start���� �������־� ���� ������ target�� �ε��� ���� ã��
���� ������ start == end �� ���, �� Ž�� ������ �ϳ��� ���� ����.
'''
def upper_target(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] > target:
        return upper_target(start, mid, arr, target)
    else:
        return upper_target(mid + 1, end, arr, target)

# target�� ���� ������ ã�� ���� ���� Ž�� �Լ�
def lower_target(start, end, arr, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] >= target:
        return lower_target(start, mid, arr, target)
    else:
        return lower_target(mid + 1, end, arr, target)


def main_func():
    for num in things:
        print(upper_target(0, n, array, num) - lower_target(0, n, array, num), end=" ")


main_func()
