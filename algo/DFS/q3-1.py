"""
2차원 배열 grid에 1은 땅, 0은 바다로 표시됩니다.
상하좌우로 연결된 1들을 한 개의 섬으로 보고, 섬의 총 개수를 구하세요.
"""


grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]

# 3


h = len(grid)
w = len(grid[0])

checked = [[False] * w for _ in range(h)]

# 상하좌우

xx = [-1, 1, 0, 0]
yy = [0, 0, -1, 1]

res = 0


def dfs(x, y):
    checked[x][y] = True

    for k in range(4):
        nx, ny = x + xx[k], y + yy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == 1 and checked[nx][ny] is False:
                dfs(nx, ny)


for i in range(h):
    for j in range(w):
        if grid[i][j] == 1 and checked[i][j] is False:
            dfs(x=i, y=j)
            res += 1


print(res)
