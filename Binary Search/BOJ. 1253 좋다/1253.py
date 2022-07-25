def make_sum_array(arr):
    new_arr = []
    zero_num = 0
    for i in range(n):
        for j in range(i + 1, n):
            new_arr.append(arr[i] + arr[j])
        if arr[i] == 0:
            zero_num += 1
    return sorted(new_arr), zero_num

def bisect_right(arr, target):
    start, end = 0, len(arr)

    while start < end:
        mid = (start + end) // 2

        if target >= arr[mid]:
            start = mid + 1

        else:
            end = mid
    return (start + end) // 2

def bisect_left(arr, target):
    start, end = 0, len(arr)

    while start < end:
        mid = (start + end) // 2

        if target > arr[mid]:
            start = mid + 1

        else:
            end = mid
    return (start + end) // 2

def main_func(array):
    answer = 0

    sum_arr, zero_num = make_sum_array(array)


    for i in array:
        # 검사하는 수가 0이라면
        if i == 0:
            # 덧셈 배열의 0의 갯수가 원래 배열의 0의 개수보다 크거나 같을 경우 정답 ++
            # 0의 경우 0이아닌 정수와 더해질 경우 0이 아닌 정수가 나오기 때문에
            if bisect_right(sum_arr, i) - bisect_left(sum_arr, i) >= zero_num:
                answer += 1
        # 검사하는 수가 0이 아니라면
        else:
            # 0이 아닌 수와 0을 더한 다면 0이 아닌 수가 나오므로 >> 0에 자기자신을 더한 경우를 제외해줘야함.
            # 덧셈 배열의 검사하는 수의 갯수가 원래 배열의 0의 개수보다 클 경우 정답 ++
            if bisect_right(sum_arr, i) - bisect_left(sum_arr, i) > zero_num:
                answer += 1

    return answer


n = int(input())
array = list(map(int, input().split()))
print(main_func(array))