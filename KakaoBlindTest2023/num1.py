'''
개인정보 1~n이 있다.
정보마다 유효기간이 있음
개인 정보마다 어떤 약관으로 수집됐는지 알고 싶다.
모든 달은 28일까지 있다.

오늘 날짜로 파기해야할 개인정보들의 번호를 구하여함.


입력 예
today: "2022.05.19"
terms: ["A 6", "B 12", "C 3"]
privacies: ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


'''
class Date:
    def __init__(self, year, month, day, number):
        self.year = year
        self.month = month
        self.day = day
        self.number = number

    def calculate(self, month):
        self.month += month
        self.year += self.month // 12
        self.month = (self.month % 12)

        if self.day == 1:
            self.month -= 1
            self.day = 28

        else:
            self.day -= 1

        if self.month < 1:
            self.year -= 1
            self.month += 12




    def __str__(self):
        return f"{self.year}: {self.month}: {self.day}"

    # 현재 날짜보다 self가 더 커야함.
    # self 가 date보다 작다면 false리턴
    def check(self, date):
        if self.year < date.year:
            return False
        elif self.year == date.year:
            if self.month < date.month:
                return False
            elif self.month == date.month:
                if self.day < date.day:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True

def solution(today, terms, privacies):
    arr = list(map(int, today.split(".")))
    today = Date(arr[0], arr[1], arr[2], 0)
    Account = [-1] * (len(privacies) + 1)
    Account[0] = today

    dic = {}
    for str in terms:
        a, b = str.split()
        dic[a] = int(b)

    for i in range(len(privacies)):
        str = privacies[i]
        date, a = str.split()
        tmp = list(map(int, date.split(".")))
        tmp_date = Date(tmp[0], tmp[1], tmp[2], i + 1)
        tmp_date.calculate(dic[a])
        Account[i + 1] = tmp_date

    answer = []
    for i in range(1, len(Account)):
        if not Account[i].check(Account[0]):
            answer.append(Account[i].number)
    return answer

a = Date(2021, 5, 1, 1)
print(a)
a.calculate(19)
print(a)


# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))



