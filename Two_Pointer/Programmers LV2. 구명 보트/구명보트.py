# 투 포인터, 그리디 문제.
def solution(people, limit):
    answer = 0
    i, j = 0, len(people) - 1
    # nlogn
    array = sorted(people)
    # n
    while i < j:
        # 양끝 사람 두명의 무게의 합이 보트 무게 제한보다 더 크다면
        if array[i] + array[j] > limit:
            # 몸무게가 큰 사람 혼자만 타고 감.
            j -= 1
            answer += 1
        # 양 끝 사람 두명의 무게의 합이 보트 무게 제한보다 작다면
        else:
            # 같이 타고감.
            i += 1
            j -= 1
            answer += 1
    # 혼자만 남았을 경우 보트하나 추가
    if i == j:
        answer += 1

    return answer
