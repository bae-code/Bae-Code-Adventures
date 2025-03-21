"""
✅ 다음 연습 문제 - “Balanced Substring”

📌 문제 설명

소문자 알파벳으로 이루어진 문자열 s가 주어진다.
이 문자열에서 ‘a’와 ‘b’의 개수가 같은 가장 긴 연속된 부분 문자열의 길이를 구해라.
	•	반드시 연속된 구간이어야 함
	•	같은 개수가 되는 가장 긴 길이를 구해야 함
"""
input = "aaabbbababaabbbaaaabbbababbababbbbaaaabbb"
def solve(ip):
    balance = 0
    first_occurrence = {0: -1}
    max_len = 0
    for i,ch in enumerate(ip):
        if ch == 'a':
            balance += 1
        else:
            balance -= 1
        
        if balance in first_occurrence:
            print(f"Balance {balance}")
            print(f"Index {i}")
            print(f"first_occ {first_occurrence[balance]}")
            print(max_len, i - first_occurrence[balance])
            print('='* 30)
            max_len = max(max_len, i - first_occurrence[balance])
        else:
            first_occurrence[balance] = i
    return max_len


a = solve(ip=input)
output = 38

print(a == output)



"""
문제 이해가 조금 어려웠네용.

balance 는 a와 b가 일치하는 구간을 구하기 위힌 변수입니다.
0일때 a,b개수가 딱맞는 구간입니다!
초기 balance 값을 -1에 둔 이유는 문자열의 맨 앞부터 a와 b가 균형을 이루는 경우를 잡기 위해서입니다.

이 문제에서 투포인터 개념은
first_first_occurrence[balance] , i 두가지가 포인터 역할을합니다.

일반적인 투포인터로 left,right 포인터를 관리하며 움직이는 구조이고,
여기서 first_first_occurrence[balance] 이것이 left 역할
i 가 right 역할을 합니다

이 경우 (i - first_occurrence[balance]) 자체가 구간의 길이 계산이기에 투포인터 개념을 가지고 있습니다.

다만 이문제에서는 포인터역할을 dict로 처리한 특징이 있습니다.


이 경우 시간복잡도는 O(N)이고, 공간복잡도는 O(N) 입니다

시간복잡도 =  문자열 순회
공간 복잡도 = first_occurrence 에 balance값이 최대 N개 저장이 되기 때문입니다.


? 추가 의문 ?
그러면 딕셔너리로 투포인터역할을 처리하지않고 처리 할 수 있는가? 

이 부분은 최소한 O(N^2)의 시간복잡도를 가지게 됩니다.

WHY?
딕셔너리의 역할 = balance의 상태값을 저장해두는 역할

포인터만 쓰게된다면 dict없이 balance상태를 기억 할 수 없기 때문에
매 left 에서 right 구간의 a,b갯수 체크를 해야해서 O(N^2)이 됩니다.

"""