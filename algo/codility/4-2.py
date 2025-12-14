"""
문제: 배열 A가 1부터 N까지 숫자가 하나씩 빠짐없이 다 들어있는지 확인하는 문제입니다.
"""
exam = [1,2,3]
def solution(A):
    # Implement your solution here
    # 중복체크 길이제기 == 최댓값 비교
    return int(max(A) == len(A) and len(set(A)) == len(A))

print(solution(A=exam))