'''
보석 공장에서 M종류의 보석을 기증했다 한종류에는 여러개의 보석이 있을 수 있다.
모든 보석을 N명의 아이들에게 나누어주려고 한다.
학생은 한 종류의 보석만 가져갈 수 있다.
질투심은 가장 많은 보석을 가져간 학생의 보석의 개수이다.
보석을 받지 않는 학생이 있어도 된다.
질투심이 최소가 되도록 보석을 나누어 주는 방법을 출력하시오

아이들의 수 : 10^9 이하
색상의 수 : 300,000 이하
각 색상당 보석의 개수: 10^9 이하

최적화 문제: 질투심의 최소값을 출력
결정 : 질투심 X로 모든 보석을 나누어 줄수 있는가?
있다면 >> 줄이기
없다면 >> 늘리기

O(Mlog 10^9) 의 알고리즘을 설계해보자.


is_possible() 함수
보석 종류를 하나씩 보며
임의의 X로 나눈 몫 + 나머지를 더함
모든 보석 종류에 대해 위를 구한 후
구한 값이 인구 수보다 크다면 False를 리턴
작거나 같다면 True를 리턴
'''

def is_possible(arr, x, people):
    number = 0
    for i in arr:
        number += i // x
        if i % x != 0:
            number += 1
    return people >= number

def parametric_search(people, arr):
    start, end = 1, int(1e9)
    while start < end:
        mid = (start + end) // 2

        if is_possible(arr, mid, people):
            end = mid

        else:
            start = mid + 1

    return (start + end) // 2


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = []
for _ in range(m):
    array.append(int(input()))
print(parametric_search(n, array))
