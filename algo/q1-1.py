"""
💡시간 복잡도 O(N)으로 풀어야 실전에서 통과 가능합니다.
연습 문제 1 - 최대 중첩 깊이 계산하기 (Difficulty: ⭐⭐)

📌 문제 설명:

괄호 문자열이 주어질 때, 가장 깊게 중첩된 괄호의 깊이를 계산하세요.

입력 예시:
s = "((())())"

출력 예시:

3

조건:
	•	문자열 길이: 1 ≤ len(s) ≤ 100,000
	•	괄호는 (와 )만 주어짐
	•	올바른 괄호 문자열만 입력으로 주어짐 (유효성 검증 필요 없음)
"""

input = "((())())"
input = "()"
input = "(()((()))())"
# input = ''

def solve(ip):
    if not ip:
        return 0
    ip = ip[1:-1]
    if not ip:
        return 1
    depth = []

    val = 1
    is_end = True
    for i in ip:
        if i == '(':
            is_end = False
            val += 1
        elif i != '(' and not is_end:
            is_end = True
            depth.append(val)
            val = 1
    
    return max(depth)


# 수학적 접근으로 새 풀이

def solve_2(ip):
    # 스택도 없으니 메모리 사용 최소화
    # CPU L1 캐시 최적화에 더 유리
    depth = 0
    max_depth = 0 
    for i in ip:
        if i == '(':
            depth += 1
            max_depth = max(depth, max_depth)
        elif i == ')':
            depth -= 1

    return max_depth

    
"""
초기 설계는 문제 조건을 바탕으로 슬라이싱 후 depth를 측정했습니다.
이 경우에는 공간 복잡도가 O(N) 으로 처리 되기때문에 문자열의 크기가 커질수록 메모리와 GC에 부하가 일어나기때문에 비효율적입니다.
하지만 확장성과 일반성을 고려했을 때, 수학적 접근으로 한 번 순회하며 최대 depth를 측정하는 것이
O(N)으로 가장 깔끔하고 공간복잡도 역시 O(1)로 돌아가기때문에 CPU 성능도 안정적으로 나올 수 있습니다.
실무에서는 후자의 방식으로 가져갈 것 같습니다.
"""


solve(ip=input)
output = 4
solve_2(ip=input)
print(solve_2(ip=input)==output)
print(solve(ip=input)==output)
    