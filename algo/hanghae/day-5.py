"""
매일 아침 9시에 학교에서 측정한 온도가 어떤 정수의 수열로 주어졌을 때,
연속적인 며칠 동안의 온도의 합이 가장 큰 값을 알아보고자 한다.
"""


n , k  = 10, 5
temps = "3 -2 -4 -9 0 3 7 13 8 -3"
temps = list(map(int,  temps.split()))


res = sum(temps[:k])              # 첫 번째 구간의 합 초기화
max_sum = res

for i in range(k, n):                 # 슬라이딩 윈도우 기법
    res = res - temps[i - k] + temps[i]        # 윈도우 이동하며 합 갱신
    print(res)
    max_sum = max(max_sum, res)

print(max_sum)