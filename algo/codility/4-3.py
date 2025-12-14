"""
문제: 배열 A에 없는 **가장 작은 양의 정수(1, 2, 3...)**를 찾으세요. (음수는 무시)
"""
exam = [-1,-3]
def solution(A):
    check = set(A)
    for i in range(1, len(A) + 2):
        if i not in check:
            return i

print(solution(A=exam))