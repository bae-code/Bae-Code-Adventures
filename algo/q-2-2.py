"""
✅ 문제 - 수열의 최대 길이 (투 포인터 기본 + 슬라이딩 윈도우)

📌 문제 설명

양의 정수로 이루어진 수열 arr가 주어진다.
이 수열의 부분 수열을 이용해 만들 수 없는 가장 작은 양의 정수를 구하라.

📌 입력
	•	첫째 줄: N (1 ≤ N ≤ 1,000)
	•	둘째 줄: 수열 arr (1 ≤ arr[i] ≤ 1,000)

📌 출력
	•	조건을 만족하는 최대 길이

입력
5
3 2 1 1 9

출력
8


입력
4
1 1 2 5

출력
10


입력
5
1 2 3 8 9

출력
7

✅ 조건
	•	시간 제한 내 O(N)으로 풀어야 통과
	•	Brute-force로 모든 구간 합 계산하면 O(N^2) → 시간 초과

✅ 힌트
	•	정렬 후 Greedy하게 접근
	•	target이 현재까지 만들 수 있는 수라면, 다음 수가 target 이상이면 break
	•	실전 코딩 테스트에서 자주 나오는 그리디 패턴
"""

input = """5
1 2 3 8 9"""

def solve(ip):
    
    data = ip.split('\n')
    max_len = int(data[0])
    int_list = list(map(lambda x: int(x),data[1].split(" ")))
    int_list.sort()
    target = 1 # 인풋에서온 조합으로 1을 만들 수 있는지 체크한다.
    for i in int_list: # 현재 숫자 i가 target보다 크다면 gap 발생
        if i > target:
            print(i,target)
            break
        target += i

    
    print(target)
    return target


solve(ip=input)

"""
📌 문제 - “수열에서 합이 K 이하인 가장 긴 연속 구간”
양수로 이루어진 수열 arr과 정수 K가 주어진다.
연속된 부분 구간 중 합이 K 이하인 가장 긴 길이를 구해라.


✅ 입력 예시
8 15
1 2 3 4 5 6 7 8

✅ 출력
5

"""

input = """8 15
1 2 3 4 5 6 7 8"""

def solve(ip):
    
    data = ip.split('\n')
    max_len = int(data[0])
    int_list = list(map(lambda x: int(x),data[1].split(" ")))
    int_list.sort()

    target = 1
    for i in int_list:
        if i > target:
            break
        target += i

    print(target)

solve(ip=input)