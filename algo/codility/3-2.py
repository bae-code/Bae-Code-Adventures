# -*- coding: utf-8 -*-

"""
문제 설명
- 배열 A에는 1부터 (N+1)까지의 숫자 중 하나가 빠져 있습니다.
- 목표: 빠진 그 하나의 숫자를 찾는 것입니다.

예시
- A = [2, 3, 1, 5]
- 1부터 5까지의 숫자 (N = len(A) = 4, N+1 = 5) 가 있어야 합니다.
- 이 경우, 빠진 숫자는 4입니다.
"""

def solution_first(A):
    """
    첫 번째 풀이:
    1부터 (N+1)까지의 총합을 구하고, 배열 A의 합을 뺍니다.
    총합 공식: n * (n + 1) / 2
    """
    n = len(A) + 1
    # 부동 소수점 나눗셈 후 정수 변환
    real_sum = int(n * (n + 1) / 2)
    sum_A = sum(A)
    # abs()를 사용하여 결과가 음수가 되지 않도록 보장
    return abs(sum_A - real_sum)

def solution_revised(A):
    """
    수정된 풀이:
    정수 나누기 연산자(//)를 사용하여 더 효율적이고 명확하게 수정합니다.
    """
    n = len(A) + 1
    # 정수 나누기를 사용하여 불필요한 형변환 제거
    real_sum = n * (n + 1) // 2
    sum_A = sum(A)
    # real_sum은 항상 sum_A보다 크거나 같으므로 abs()가 필요 없습니다.
    return real_sum - sum_A

# --- 테스트 ---
if __name__ == "__main__":
    exam = [2, 3, 1, 5]
    
    print("### 문제 예시 ###")
    print(f"배열 A = {exam}\n")

    print("--- 첫 번째 풀이 결과 ---")
    result_first = solution_first(exam)
    print(f"빠진 숫자: {result_first}\n")

    print("--- 수정된 풀이 결과 ---")
    result_revised = solution_revised(exam)
    print(f"빠진 숫자: {result_revised}\n")
    
    # 두 결과 비교
    assert solution_first(exam) == solution_revised(exam)
    print("✅ 두 풀이의 결과가 동일합니다.")
