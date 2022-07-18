'''
투포인터 문제

무조건 담을 용액을 하나 지정해두고 >> 순처적으로 탐색하며 지정 >> O(n)
    지정한 용액을 기준으로 투포인터를 돌려서 나머지 두 용액을 지정. >> O(n)
    >> 최적화 포함.
time complexity >> O(n^2)
n 이 5000개이므로 충분히 가능
'''
def Two_Pointer(arr):
    min_d = float('inf')
    ans_s, ans_e, ans_t = -1, -1, -1
    # n
    for tmp in range(len(arr)):

        start, end = 0, len(arr) - 1
        # n
        while start < end:
            tmp_sum = arr[tmp] + arr[start] + arr[end]

            # 중복 제거
            if start == tmp:
                start += 1
                continue

            if end == tmp:
                end -= 1
                continue
            # 최적화
            if abs(tmp_sum) < min_d:
                ans_s, ans_e, ans_t, min_d = start, end, tmp, abs(tmp_sum)

            # 포인터 이동
            if tmp_sum == 0:
                return " ".join(map(str, sorted([arr[start], arr[end], arr[tmp]])))

            elif tmp_sum > 0:
                end -= 1

            else:
                start += 1

    return " ".join(map(str, sorted([arr[ans_s], arr[ans_t], arr[ans_e]])))

n = int(input())
array = sorted(list(map(int, input().split())))
print(Two_Pointer(array))