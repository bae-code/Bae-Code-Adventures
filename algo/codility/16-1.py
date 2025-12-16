k = 4
a = [1,2,3,4,1,1,3]

# k = 5
# a = [3,3]
"""
줄의 길이 배열 A와 목표길이 K 가 주어진다.
인접한 줄을 묶어서 길이가 K이상인 줄을 최대한 많이 만들어라.
"""


def solution(K, A):
    current_length = 0
    cnt = 0 
    for i in A:
        # 1. 일단 묶는다 (조건 없이 더함)
        current_length += i
        # 2. 묶은 게 K 이상이면? (같거나 커지면)
        if current_length >= K:
            cnt += 1           # 성공!
            current_length = 0 # 가위로 자름 (리셋)
            
    return cnt
            

print(solution(K=k,A=a))