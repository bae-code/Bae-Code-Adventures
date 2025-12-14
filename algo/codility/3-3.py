# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
"""
문제: 배열 A를 어느 지점 P에서 두 동강 냈을 때,
 **|왼쪽 합 - 오른쪽 합|**의 최솟값을 찾아라.
 예시: A = [3, 1, 2, 4, 3]
 P=1에서 자르면: 왼쪽 [3], 오른쪽 [1, 2, 4, 3] > |3 - 10| = 7
 P=2에서 자르면: 왼쪽 [3, 1], 오른쪽 [2, 4, 3] > |4 - 9| = 5... 
 이 중에서 가장 작은 값을 리턴해야 합니다.
"""
exam = [3, 1, 2, 4, 3]

def solution(A):
    # 전체 합을 구한다
    minimal = float('inf')
    total = sum(A)
    left = 0 
    for P in A[:-1]:
        left += P
        right = total - left
        value = abs(left - right)
        if  value <= minimal:
            minimal = value
    return minimal

print(solution(A=exam))