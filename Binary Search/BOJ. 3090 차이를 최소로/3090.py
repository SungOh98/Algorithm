def is_possible(arr, x, t, n):
    cnt = 0
    # 그리디 전략 : 바로 앞이 X이상 차이난다면 깍아버려
    # 깍는 양은 최소로

    for i in range(n - 1):
        if arr[i + 1] - arr[i] > x:
            cnt += arr[i + 1] - (x + arr[i])
            arr[i + 1] = arr[i] + x

    for i in range(n - 1, 0, -1):
        if arr[i - 1] - arr[i] > x:
            cnt += arr[i - 1] - (x + arr[i])
            arr[i - 1] = arr[i] + x

    return cnt <= t, arr


def parametric_search():
    start, end = 0, int(1e9)
    answer = -1
    while start < end:
        mid = (start + end) // 2
        flag, tmp = is_possible(array[:], mid, t, n)
        if flag:
            end = mid
            answer = tmp
        else:
            start = mid + 1
    return " ".join(map(str, answer))

n, t = map(int, input().split())
array = list(map(int, input().split()))
print(parametric_search())