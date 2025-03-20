"""
주어진 문자열 리스트에서 각 문자열이 올바른 괄호 열림/닫힘 순서를 따르는지 판별하는 문제입니다.
•	{}, [], () 괄호들이 짝을 맞춰 올바르게 닫혀야 함
•	중간에 잘못된 순서가 나오면 "NO"
•	모든 괄호가 올바르게 닫히면 "YES"
example
input:
['{}[]()', '{[}]}', '{{', '{[]}']
output:
['YES', 'NO','NO', 'YES']
"""
import textwrap
input = ['{}[]()', '{[}]}', '{{', '{[]}']

def braces(ip):
    results = []
    correct_match_map = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    start_barce = '{[('
    for s in ip:
        result = "YES"
        if len(s) % 2 != 0:
            result = "NO"
        
        brace_stack = []
        for i in s:
            if i in start_barce:
                brace_stack.append(i)
            else:
                if not brace_stack:
                    result = "NO"
                    break
                #닫는 케이스
                if i == correct_match_map[brace_stack[-1]]:
                    brace_stack.pop()
                else:
                    result = "NO"
                    break
        if brace_stack:
            result = "NO"

        results.append(result)
        
    return results


test = braces(input)
print(test)
output = ['YES', 'NO','NO', 'YES']
print(test == output )



