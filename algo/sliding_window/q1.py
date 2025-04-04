"""
DNA 문자열은 모든 문자열에 등장하는 문자가 {‘A’, ‘C’, ‘G’, ‘T’} 인 문자열을 말한다. 
DNA 문자열 길이 |S|
부분문자열의 길이 |P|

두번 째 줄에는 민호가 임의로 만든 DNA 문자열이 주어진다.

세번 째 줄에는 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수가 공백을 구분으로 주어진다.
각각의 수는 |S| 보다 작거나 같은 음이 아닌 정수이며 총 합은 |S| 보다 작거나 같음이 보장된다.

"""

from collections import Counter, defaultdict

s , p = map(int, input().split())
pass_str = input()
gte_dict = defaultdict(int)

gte_dict["A"], gte_dict["C"], gte_dict["G"], gte_dict["T"] = map(int, input().split())

res = 0

password = pass_str[:p]

init_window = defaultdict(int)

for char in password:
    init_window[char] += 1

def check():
    for k in "ACGT":
        if init_window[k] < gte_dict[k]:
            return False
    return True

if check():
    res += 1

for i in range(1, s - p + 1):
    out_char = pass_str[i - 1]
    in_char = pass_str[i + p - 1]
    init_window[out_char] -= 1
    init_window[in_char] += 1

    if check():
        res += 1
    
    
print(res)
    
    
