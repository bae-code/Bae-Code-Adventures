# N 초 동안 싸움을 함 . 
# 플레이하는 캐릭은 A,B 를 사용할수있다 스킬
# a는 1초 b는 m초의 시전시간이다.
# n이 4초이고 m이 2초이면 aaaa,aab,aba,bb로 5가지가 가능

# 입력
# 첫 번째 줄에 싸움 시간 N과 B 스킬의 시전 시간 M이 주어진다. (N은 10,000 이하의 자연수, M은 2 이상 100 이하의 자연수)

# 출력
# 가능한 조합의 수를 1,000,000,007로 나눈 나머지 값을 출력한다.

nanoom = 1_000_000_007

n  = 120
m = 60
a =  1
n,m = map(int,input().split())

dp = [0] * (n+1)

dp[0] = 1

for i in range(1, n + 1):

    dp[i] += dp[i-1]

    if i >= m:
        dp[i] += dp[i - m]

    dp[i] %= nanoom

print(dp[n])