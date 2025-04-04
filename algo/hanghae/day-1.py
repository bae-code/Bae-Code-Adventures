"""
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

예제 입력 1
3 16
예제 출력 1
3
5
7
11
13
"""

a = "3 16"


def solve():
    a, b = map(int, input().split())
    is_prime = [True] * (b + 1)

    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(b**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, b + 1, i):
                is_prime[j] = False

    for x in range(a, b + 1):
        if is_prime[x]:
            print(x)


solve()


"""
위 문제는 실행시간에 대한 조건이 2.5초로 제한이 되어있어서, 일반적인 방법으로는 완료할수없다.

그래서 사용한것이 에라토스테네스의 체 입니다.

"""
