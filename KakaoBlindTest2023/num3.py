'''
카카오톡은 이모티콘 플러스 서비스 가입자를 늘리려고 한다.
할인 행사
목표 > 우선순위에 따른
1. 이모티콘 플러스 가입자를 최대한 늘리는 것
2. 이모티콘 판매액을 최대한 늘리는 것

할인 행사
n명의 회 m개의 이모티콘
이모티콘 마다 할인 율은 10 20 30 40 퍼 중 하나

회원들은 다음의 기준에 따라 이모티콘을 사거나 이모티콘 플러스에 가입함
1. 각 사용자는 자신의 기준에 따라 일정 비율이상 할인하는 이모티콘을 모두 구매함.
2. 각 사용자는 자신의 기준에 따라 이모티콘 구매 비용의 합이 일정 자격 이상 된다면 이모티콘 구매를 모두 취소하고 이모티콘 플러스에 가입함.

1 <= 사용자수 n <= 100
1 <= 비율 <= 40
100 <= 가격 <= 1,000,000
1 <= 이모티콘 개수 m <= 7
100 <= 이모티콘의 가격 <= 1,000,000
이 주어졌을 때
행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스의 가입자 수와 이모티콘 매출을 출력하시오

비율이 정해짐 -> 가격이 정해짐 -> 가입자 수 와 매출액이 정해짐
걍 브루트포스 아닌가?
아 이모티콘 마다 할인율이 다르구나!
4 * 7의 경우의 수 가 있다.

각 이모티콘 별 할인율 지정 -> 할인율 고려하여 사용자별 구매 이모티콘 확정 -> 사용자별 구매금액을 통한 이모티콘 플러스 가입 여부 확정 -> 매출액 확정
users : [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]

emoticons : [1300, 1500, 1600, 4900]

'''
'''
n = int(input())
percent = float(input())
print(n -  n * percent / 100)
'''
case = []


def solution(users, emoticons):
    answer_list = []
    make_case(len(emoticons), 0, [])
    # print(case)
    for cnt_case in case:
        plus_num, profit = 0, 0
        for user in users:
            tmp = phrase(user, emoticons, cnt_case)
            plus_num += tmp[0]
            profit += tmp[1]

        answer_list.append([plus_num, profit])

    answer_list.sort(key=lambda x: (-x[0], -x[1]))
    return answer_list[0]


def make_case(n, idx, tmp):
    global case
    if idx == n:
        case.append(tmp)
        return

    for i in (10, 20, 30, 40):
        make_case(n, idx + 1, tmp + [i])


# 할인율 케이스와 유저 1명을 입력 받고 할인율에 따라 계산하여 유저가 가입한 플러스 정보, 유저가 낸 돈의 정보를 리턴
def phrase(user, emoticons, cnt_case):
    user_sale, user_money = user[0], user[1]
    need_money = 0
    for i in range(len(cnt_case)):
        if cnt_case[i] >= user_sale:
            need_money += (emoticons[i] - emoticons[i] * cnt_case[i] / 100)

    if need_money >= user_money:
        user_plus = 1
        need_money = 0
    else:
        user_plus = 0

    return user_plus, need_money

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))