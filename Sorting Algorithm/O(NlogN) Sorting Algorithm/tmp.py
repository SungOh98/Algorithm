import random
import time


def main():

    ###################
    #   Create List   #
    ###################

    n = int(input("배열의 크기 입력: "))
    TRIAL = int(input("TRIAL 입력: "))
    s = []

    for i in range(n):
        s.append(random.randint(0, n))

    s1 = s.copy()
    s2 = s.copy()
    s.sort()

    # print("s1:", s1)  # merge sort
    # print("s2:", s2)  # quick sort
    # print()

    ##################
    #   Merge Sort   #
    ##################

    start = time.time()
    merge_sort(s=s1, low=0, high=len(s2) - 1)
    end = time.time()
    print("[Merge Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    # print("s1:", s1)
    print("Correct:", s == s1)
    print()

    ##################
    #   Quick Sort   #
    ##################

    start = time.time()
    quick_sort(s=s2, low=0, high=len(s2) - 1)
    end = time.time()
    print("[Quick Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    # print("s2:", s2)
    print("Correct:", s == s2)
    print()

    #############
    #   TRIAL   #
    #############

    # TRIAL = 100

    total_elapsed_time_merge_sort = 0
    total_elapsed_time_quick_sort = 0

    print("[progressing] - TRIAL: {}".format(TRIAL))
    print(">" * (TRIAL // (TRIAL // 20)))

    for trial in range(TRIAL):
        # Create list
        # n = 5000
        s = []
        for i in range(n):
            s.append(random.randint(0, n))

        s1 = s.copy()
        s2 = s.copy()

        # Merge Sort
        start = time.time()
        merge_sort(s=s1, low=0, high=len(s2) - 1)
        end = time.time()
        total_elapsed_time_merge_sort += end - start

        # Merge Sort
        start = time.time()
        quick_sort(s=s2, low=0, high=len(s2) - 1)
        end = time.time()
        total_elapsed_time_quick_sort += end - start

        if TRIAL >= 20 and (trial + 1) % (TRIAL // 20) == 0:
            print(">", end="", flush=True)

    print()
    print("Merge Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_merge_sort))
    print("Merge Sort - Average Elapsed Time: {:.5}s".format(total_elapsed_time_merge_sort / TRIAL))
    print()
    print("Quick Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_quick_sort))
    print("Quick Sort - Average Elapsed Time: {:.5}s".format(total_elapsed_time_quick_sort / TRIAL))


def merge_sort(s, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(s, low, mid)
        merge_sort(s, mid + 1, high)
        merge(s, low, mid, high)


def merge(s, low, mid, high):
    tmp = [0] * (high - low + 1)
    i = low
    j = mid + 1
    t = 0
    # 나누어진 두 배열의 순서를 나태는 두 인덱스 변수가 모두 배열 범위 안 일동안 반복
    while i <= mid and j <= high:
        # 앞의 배열의 원소가 더 작을 경우
        if s[i] <= s[j]:
            # 임시 배열에 그 원소 대입
            tmp[t] = s[i]
            # 다음 것 보기.
            t += 1
            i += 1
        # 뒤의 배열의 원소가 더 작을 경우
        else:
            tmp[t] = s[j]
            t += 1
            j += 1
    # 앞 배열의 끝까지 안 갔을 경우 끝까지 보며 tmp에 모두 채워 넣기
    while i <= mid:
        tmp[t] = s[i]
        t += 1
        i += 1

    # 앞 배열의 끝까지 안 갔을 경우 끝까지 보며 tmp에 모두 채워 넣기
    while j <= high:
        tmp[t] = s[j]
        t += 1
        j += 1
    # tmp에 모두 집어 넣었으니 다시 s에 copy

    i, t = low, 0
    while i <= high:
        s[i] = tmp[t]
        i += 1
        t += 1


def quick_sort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quick_sort(s, low, pivot - 1)
        quick_sort(s, pivot + 1, high)


def partition(s, low, high):
    # 기준 원소
    x = s[high]
    # pivot 보다 작은 원소들을 왼쪽으로 배치하기 위한 변수 >> i
    i = low - 1
    # low 부터 피벗 전까지 탐색
    for j in range(low, high):
        # 피벗값보다 현재 탐색 원소가 작거나 같다면
        if s[j] <= x:
            # i 를 1 더해주고
            i += 1
            # j 값과 swap
            s[i], s[j] = s[j], s[i]
            # if 문 안쪽이 피벗 보다 작은 값들을 피벗 왼쪽으로 위치시키는 과정이다.
    # for문을 통해 모두 배치시켰다면 피벗을 위치시킴
    i += 1
    s[i], s[high] = s[high], s[i]

    # 피벗의 위치를 리턴
    return i

def check(sort):
    array = list(map(int, input("배열 공백을 두고 입력: ").split()))

    if sort == "merge":
        print(f"정렬 전: {array}")
        merge_sort(array, 0, len(array) - 1)
        print(f"정렬 후: {array}")

    else:
        print(f"정렬 전: {array}")
        quick_sort(array, 0, len(array) - 1)
        print(f"정렬 후: {array}")

if __name__ == "__main__":
    main()
# order = input("무슨 정렬 테스트할래? (merge or quick):")
#
# check(order)
