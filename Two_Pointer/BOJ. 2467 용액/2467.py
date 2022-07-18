'''
많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다.
특성값 : 용액의 산도 를 숫자로 표현

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 두 용액의 특성값의 합으로 정의된다.
연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0 에 가까운 용액을 만들려고 한다.

산성용액과 알칼리성 용액의 특성값이 정렬된 순서대로 주어졌을 때 이중 두개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오

답이 여러개라면 아무거나 출력
두 특성값은 오름차순으로 출력

특성값: -1_000_000_000 ~ 1_000_000_000
용액의 갯수: 2~ 100,000 개

nlogn까지 허용하는 문제이다.

나는 투포인터를 활용해서 풀어보고자 한다.


'''
def Two_Pointer(array):
    start, end, min_d = 0, len(array) - 1, float('inf')
    # 투 포인터가 겹처지면 종료
    ans_s, ans_e = -1, -1
    # O(n)의 시간 복잡도로 해결!
    while start < end:
        tmp = array[start] + array[end]

        # 최적화
        if abs(tmp) < min_d:
            min_d = abs(tmp)
            ans_s, ans_e = start, end

        if tmp == 0:
            return f"{array[start]} {array[end]}"
        elif tmp > 0:
            end -= 1
        else:
            start += 1
    return f"{array[ans_s]} {array[ans_e]}"


n = int(input())
array = list(map(int, input().split()))

print(Two_Pointer(array))
