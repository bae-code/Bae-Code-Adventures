"""
📝 문제 이름:

Programmer's String

📌 문제 설명:

길이가 N인 문자열이 주어집니다.
문자열에서 단어 "programmer"를 두 번 포함하는 구간을 찾으세요.
	•	첫 번째 "programmer"는 왼쪽부터 탐색
	•	두 번째 "programmer"는 오른쪽부터 탐색
	•	두 "programmer" 사이에 존재하는 문자 개수를 구하세요

단, 중복 사용은 불가능합니다.

📌 입력:
	•	문자열 s (1 ≤ len(s) ≤ 10^5)
	•	문자열은 소문자 알파벳으로만 구성됨

📌 출력:
	•	두 "programmer" 사이의 문자 개수 (0 이상)

Input: "progxrammerrxproxgrammer"
Output: 2

Input: "programmerprogrammer"
Output: 0

Input: "programmerxabcxprogrammer"
Output: 5

"""

input = "programmerxabcxprogrammer"


def solve(ip):
    match = "programmer"
    start_pointer = 0
    end_pointer = len(match) - 1

    result = 0
    for i in range(len(ip)):
        if ip[i] == match[start_pointer]:
            start_pointer += 1
            if start_pointer == len(match):
                left_end = i
                break

    for j in range(len(ip) - 1, start_pointer, -1):
        if ip[j] == match[end_pointer]:
            end_pointer -= 1
            if end_pointer < 0:
                right_start = j
                break

    result = right_start - left_end - 1
    return result


# 투포인터에 대해 알았다.
# 인덱스를 다루는 연습이 조금 미흡했다.
# 두 루프 모두 O(N)이지만 직렬 실행이기때문에 시간 복잡도는 O(N) 이다
# 공간복잡도는 O(1)


a = solve(ip=input)
print(a)
