"""
💡시간 복잡도 O(N)으로 풀어야 실전에서 통과 가능합니다.
연습 문제 2 - 최소 괄호 추가 (Difficulty: ⭐⭐⭐)

📌 문제 설명:

괄호 문자열이 주어질 때, 올바른 괄호 문자열로 만들기 위해 추가해야 하는 최소 괄호의 개수를 구하세요.

📌 입력 예시:
s = "())("
출력 예시:
2
 조건:
	•	문자열 길이: 1 ≤ len(s) ≤ 100,000
	•	괄호는 (와 )만 주어짐
"""
input = "())(()"
input = "((())((())"
input = ")()))"


def solve(ip):
    result = 0
    final = 0
    for i in ip:
        if i == "(":
            if result <= 0:
                result = 0
            result += 1
        else:
            if result <= 0:
                final += 1
            result -= 1
    if result > 0:
        return final + result
    return final


a = solve(ip=input)
output = 3
print(a == output)
