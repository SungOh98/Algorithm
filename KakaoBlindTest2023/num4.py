'''
이진 트리를 수로 표현하자

방법
1. 이진수를 저장할 빈 문자 생성
2. 주어진 이진 트리에 더미 노드를 추가하여 포화 이진 트리로 만듭니다. -> 루트노드는 그대로 유지
3. 만들어진 포화 이진트리의 노드들을 가장 왼쪽 부터 오른쪽 까지 순서대로 살핌 - 노드의 높이는 무시가능
4. 살펴본 노드가 더미노드라면 문자열 뒤에 0추 더미가 아니면 1 추가
5. 문자열에 저장된 이진수를 십진수로 변환

루트노드는 왼쪽 서브트리의 노드들 보다 오른쪽에 존재
루트노드는 오른족 서브트리의 노드들보다 왼쪽에 존재

numbers가 주어질때 주어진 수를 이진 트리로 표현 가능한기?
가능하면 1 가능하지 않다면 0

1 <= 숫자 개수 <= 10,000
1 <= 숫자 크기 <= 10^15

뭔가 이분 탐색 삘이 난디.
부모 노드가 0인데 자식노드가 1이면 안됨.
주어진 수 -> 이진수 변환 -> 리스트에 삽입 -> 나머지 0 삽입 -> root노드 구하기

'''
# print(bin(58))
# a = bin(58)[2:]
# print(a)

answer = True
def binary_search(string, start, end):
    global answer
    if (start >= end):
        return
    root = (start + end) // 2
    left = (start + root - 1) // 2
    right = (root + end + 1) // 2

    binary_search(string, start, root - 1)
    binary_search(string, root + 1, end)

    if string[root] == "0" and (string[left] == '1' or string[right] == '1'):
        answer = False
        return
# a = bin(int(input()))[2:]
# binary_search('0' + a, 1, len(a))
# print(answer)

def solution(numbers):
    global answer
    ans = []
    for number in numbers:
        bin_num = bin(number)[2:]
        bin_num = "0" * (Zero(len(bin_num)) - len(bin_num)) + bin_num
        # print(bin_num)
        answer = True
        binary_search(bin_num, 1, len(bin_num) - 1)
        if answer:
            ans.append(1)
        else:
            ans.append(0)
    return ans


def Zero(bit_num):
    cnt = 0
    mul = 0
    while cnt < bit_num:
        cnt += 2 ** mul
        mul += 1
    return cnt

# print(Zero(1))
print(solution([63, 111, 95]))

