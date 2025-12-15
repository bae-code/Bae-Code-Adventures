
"""
가볍게 몸풀기부터 시작합시다.
이 문제는 누적 합의 '개념'을 이용하는 논리 문제입니다.
상황:
0: 동쪽(East)으로 가는 차 ($\rightarrow$)
1: 서쪽(West)으로 가는 차 ($\leftarrow$)
목표: 서로 마주치며 **스쳐 지나가는 차의 쌍(Pair)**이 몇 개인지 구하세요.
(0이 먼저 나오고, 그 뒤에 나오는 1들과 짝을 이룸)
예시: A = [0, 1, 0, 1, 1]
첫 번째 0: 뒤에 1이 3개 있음 $\rightarrow$ 3쌍
두 번째 0: 뒤에 1이 2개 있음 $\rightarrow$ 2쌍
총 5쌍
"""
exam = [0,1,0,1,1]
def solution(A):
    zero_cnt = 0
    pair = 0
    for v in A:
        if v == 0:
            # 0이 나오면 오른쪽으로 가는차 카운트를 함
            zero_cnt +=1
        else:
            # 1이 나오면 현재까지나온 오른쪽으로 가는 차를 모두 만났다.
            pair += zero_cnt
    if pair > 1_000_000_000:
        return -1
    return pair
print(solution(A=exam))