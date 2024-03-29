'''
옥토끼는 총 N개의 문제를 풀어야 하며 각 문제마다 푸는데 걸리는 시간이 다르다.
옥토끼는 한번에 두개의 문제를 동시에 풀 수 있다.
한번 풀기 시작한 문제는 멈추지 않으며 항상 문제를 풀고 있을 필요는 없다.
감시자는 옥토끼가 문제를 해결한 시점만 볼 수 있을 뿐 옥토끼가 지금 쉬고 있는지 문제를 풀고 있는지 모른다.
다만 옥토끼가 문제하나를 풀고나서 다음 문제를 풀때까지의 걸리는 시간이 길어지면 감시자의 독촉이 심해지기 때문에
이 간격의 최대값을 최소로 하려고한다.

파라메트릭 서치
임의의 구간 사이의 최대값 S를 정한다.
구간 사이의 최대값 S로 문제를 풀 수 있는가?
있다면 줄이기
없다면 늘리기.

결정함수
임의의 S간격으로 문제들을 배치할 수 있는지 없는지만 판단하면 된다.
배치할 수 있다면 S를 줄여서 다시 확인한다
배치할 수 없다면 S를 늘릴 수 밖에 없다.

결정함수를 NlogN에 해결해야함.

한 구간에 3개 이상의 작업을 처리하면 안됨.
s * i 시점에 무조건 끝내는 작업이 있어야한다(i 는 1 2 3 4...)

'''