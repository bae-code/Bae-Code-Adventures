"""
행과 열의 크기  N 
높이정보는 N * N  2차원 배열 형태로 주어짐
각 원소는 지점 높이 표시 

아무 지역도 물에 잠기지 않을 수도 있다.

어떤 지역의 높이 정보가 주어졌을 때,
장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오.

첫째 줄에 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 출력한다.
"""
N = 4
grid = """1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1"""


grid = list(map(lambda x: list(map(int, x.split(" "))), grid.split("\n")))


max_rain = max(max(grid))


# 상하좌우

xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]

res = 0

# 0 부터 최대 높이 이하까지 반복


def dfs(x, y, rain):
    checked[x][y] = True
    for k in range(4):
        nx, ny = x + xx[k], y + yy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny] > rain and checked[nx][ny] is False:
                dfs(nx, ny, rain)


for rain in range(max_rain + 1):
    count = 0
    checked = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if grid[i][j] > rain and checked[i][j] is False:
                dfs(x=i, y=j, rain=rain)
                count += 1
    res = max(res, count)


print(res)
