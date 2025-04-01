"""
문제
피보나치 비스무리한 수열은 f(n) = f(n-1) + f(n-3)인 수열이다.
f(1) = f(2) = f(3) = 1이며 피보나치 비스무리한 수열을 나열하면 다음과 같다.

1, 1, 1, 2, 3, 4, 6, 9, 13, 19, ...

자연수 n을 입력받아 n번째 피보나치 비스무리한 수열을 구해보자!

입력

자연수 n(1 ≤ n ≤ 116)이 주어진다.

출력
n번째 피보나치 비스무리한 수를 출력한다.

예제 입력 1 

10

예제 출력 1 

19
"""


a = 10


def fivo(n):
    if n <= 3:
        return 1
    dp = [0] * (n + 1)

    dp[1] = dp[2] = dp[3] = 1  # 초기값 정의
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]  # 점화식 적용
    return dp[n]


fivo(a)




def fivo(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 3:
        return 1
    
    memo[n] = fivo(n -1 , memo) + fivo(n-3 , memo)

    return memo[n]

print(fivo(10))