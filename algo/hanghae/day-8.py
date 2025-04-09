"""
첫째 줄에 파일의 개수 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄에는 패턴이 주어진다. 패턴은 알파벳 소문자와 별표(아스키값 42) 한 개로 이루어져 있다. 문자열의 길이는 100을 넘지 않으며, 별표는 문자열의 시작과 끝에 있지 않다.

다음 N개 줄에는 파일 이름이 주어진다. 파일 이름은 알파벳 소문자로만 이루어져 있고, 길이는 100을 넘지 않는다.


총 N개의 줄에 걸쳐서, 입력으로 주어진 i번째 파일 이름이 패턴과 일치하면 "DA", 일치하지 않으면 "NE"를 출력한다.

참고로, "DA"는 크로아티어어로 "YES"를, "NE"는 "NO"를 의미한다.


3
a*d
abcd
anestonestod
facebook

###out put###
DA
DA
NE
"""

import sys
import re

n = int(input())
start,end = input().split("*")
lines = sys.stdin.read().splitlines()
pattern = rf"^{start}.*{end}$"

for x in range(n):
    if re.match(pattern=pattern,string= lines[x]):
        print('DA')
    else:
        print("NE")


