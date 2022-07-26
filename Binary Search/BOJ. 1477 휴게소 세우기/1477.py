'''
휴게소 세우기
유료 고속도로에 휴게소가 있다. 각 휴게소는 고속도로의 시작위치로부터 얼마만큼 떨어져 있는지 안다.
다솜이는 여기에 휴게소 M개를 추가로 설치하려고 한다.
규칙
1. 이미 휴게소가 있는 장소와 고속도로의 끝지점에는 세울 수 없다.
2. 다솜이는 휴게소 M개를 모두 지어서 고속도로에 휴게소가 없는 구간의 길이를 최소화하려고 한다.


파라 메트릭 서치

최적화 문제: 휴게소들 사이의 거리가 최소
결정 문제 : 임의로 설정한 휴게소들 거리 x가 설치 가능한가? 아닌가? !!!!


'''


# m: 추가로 설치할 휴게소 개수
# x: 임의로 설정한 휴게소 사이의 거리

# 임의로 설정한 X에 대한 결정함수

def is_possible(arr, m, x):
    # 두 개의 휴게소 사이에서 휴게소들의 거리가 X 이하가 되도록 휴게소들을 설치함.
    # m개를 모두 소진해도 거리를 X 이하로 좁힐 수 없다면 False를 리턴
    # m개를 모두 소진하지 않고 거리를 X이하로 좁힐 수 있다면 >> 매개변수 X를 더 많이 줄일 수 있다.


    for i in range(len(arr) - 1):
        start, end = arr[i], arr[i + 1]
        middle = start

        while m > 0:
            middle += x
            if middle >= end:
                break
            m -= 1

        # m개를 모두 소진하면 멈춤!

        if m <= 0 and end - middle > x:
            return False

    return True

def parametric_search(arr, m):
    start, end = 0, l
    while start < end:
        parameter = (start + end) // 2
        # 70 미만이면 >> False
        if is_possible(arr, m, parameter):
            end = parameter
        else:
            start = parameter + 1

    return (start + end) // 2



n, m, l = map(int, input().split())
#
array = sorted(list(map(int, input().split())) + [0] + [l])

# print(is_possible(array, 5, 70))
print(parametric_search(array, m))