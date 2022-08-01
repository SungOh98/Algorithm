'''
놀이 공원
M개의 1인승 놀이기구 존재
놀이기구는 각각 운행시간이 정해짐
놀이기구가 비어있으면 현재 줄에서 가장 앞에 있는 아이가 빈 놀이기구에 탑승한다.
만일 여러개의 놀이기구가 동시에 비어있다면 더 작은 번호가 적혀 있는 놀이기구에 탑승한다.

놀이기구가 모두 비어있는 상태에서 시작할 때, 줄의 마지막 아이가 타게 되는 놀이기구 번호를 구하시오
아이들 최대 20억 명 , 놀이기구 최대 1만 대
운행 시간은 1이상 30이하의 자연수

최악의 경우
이용시간 모두 30
놀이기구 수 10000
인구수 20억
간단한 알고리즘으로는 O(MN)을 생각해볼 수 있겠다.
당연히 시간 초과

입국 심사 문제 처럼 시간으로 파라메트릭 서치를 접근해보자.
모든 아이들을 놀이기구에 탑승시킬 최대 시간 : 20억 * 30


파라메트릭 서치 알고리즘


'''


def get_surplus(time, plays, people):
    for i in range(1, len(plays)):
        people -= (time // plays[i] + 1)
    # 놀이기구를 주어진 시간동안 태우고 남은 아이들의 숫자를 리턴함.
    # 0또는 음수가 나올 경우 아이들을 모두 태운 것
    return people

def surplus_to_answer(plays, surplus, time):
    for i in range(m, 0, -1):
        if time % plays[i] == 0:
            if surplus >= 0:
                return i
            else:
                surplus += 1



# print(is_possible(8, [0, 3, 4, 2, 5, 1], 22))

def parametric_search(plays, people):
    start, end = 0, n * 30

    while start < end:
        time = (start + end) // 2
        surplus = get_surplus(time, plays, people)
        # 아이들을 모두 태운 경우임. >> 시간 줄여
        if surplus <= 0:
            end = time

        else:
            start = time + 1

    surplus = get_surplus((start + end) // 2, plays, people)
    return surplus_to_answer(plays, surplus, (start + end) // 2)

n, m = map(int, input().split())
plays = [0] + list(map(int, input().split()))

print(parametric_search(plays, n))
