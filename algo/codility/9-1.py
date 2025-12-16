
a = [23171, 21011, 21123, 21366, 21013, 21367]
def solution(A):
    max_profit = 0
    min_price = float('inf')
    
    for i in A:
        if i < min_price:
            # 최저가를 갱신한다 (파는날은 사는날보다 항상 뒤이기 때문)
            min_price = i

        # 최대이익을 저장한다
        max_profit = max(max_profit, i - min_price)

    return max_profit


print(solution(A=a))