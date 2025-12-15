"""
A 배열: 물고기의 크기 (모두 다름)
B 배열: 물고기의 이동 방향 
(0: 상류/왼쪽 $\leftarrow$, 1: 하류/오른쪽 $\rightarrow$)
규칙:서로 다른 방향으로 가는 물고기가 마주치면 싸움이 일어납니다.
크기가 큰 물고기가 작은 물고기를 잡아먹습니다. (작은 놈은 사라짐)
같은 방향으로 가는 물고기는 서로 잡아먹지 않습니다.
목표: 싸움이 다 끝나고 살아남은 물고기는 몇 마리인가?
"""
a ,b = [4, 3, 2, 1, 5], [0, 1, 0, 0, 0]

def solution(A,B):
    right = []
    alive = 0
    right_num = 1
 
    for size , way in zip(A,B):
        if way == right_num:
            right.append(size)
        else:
            while right:
                if right[-1] > size:
                    break
                else:
                    right.pop()
            if not right:
                alive += 1
    return alive + len(right)
print(solution(A=a,B=b))
            
            