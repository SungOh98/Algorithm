'''
알고리즘
순차적으로 하나의 수를 고름
고른 하나의 수에 대해 다음과 같은 투포인터 알고리즘 적용
1. start와 end 두 포인터를 배열과 양끝에 설정. >> end가 start보다 클때까지 반복!
2. 고른 하나의 수에 부호를 바꾼 수보다 arr[start] + arr[end]가 크다면 end -= 1, 작다면 start += 1
                                            같다면 bisect_left, bisect_right를 구하여 정답에 추가 후 start, end를 조정.

'''


def bisect_right(start, end, arr, target):
    while start < end:

        mid = (start + end) // 2

        if arr[mid] <= target:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2


def bisect_left(start, end, arr, target):
    while start < end:

        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1

        else:
            end = mid

    return (start + end) // 2


def Two_Pointer(arr, start, end, target):
    plus = 0
    while start < end:
        sub_sum = arr[start] + arr[end]

        if sub_sum > target:
            end = bisect_left(start, end, arr, arr[end]) - 1

        elif sub_sum < target:
            start = bisect_right(start, end, arr, arr[start])

        else:
            # 두개의 포인터가 가리키는 값이 같을 경우 조합으로 경우의수를 계산 후 리턴
            if arr[start] == arr[end]:
                com = end - start + 1
                plus += (com * (com - 1)) // 2

                return plus

            # 두개의 포인터가 가리키는 값이 다를 경우
            plus += (bisect_right(0, len(arr), arr, arr[start]) - start) * (
                        end - bisect_left(0, len(arr), arr, arr[end]) + 1)

            start = bisect_right(0, len(arr), arr, arr[start])
            end = bisect_left(0, len(arr), arr, arr[end]) - 1

    return plus


def main_func():
    answer = 0

    for i in range(len(array) - 2):
        answer += Two_Pointer(array, i + 1, len(array) - 1, -array[i])
    return answer


n = int(input())
array = sorted(list(map(int, input().split())))
print(main_func())
