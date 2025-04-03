
"""
0은 길, 1은 벽

(0,0)에서 시작해서 (n-1, m-1)로 도달 가능한지 DFS로 판별하세요.

도달할 수 있다면 True, 아니면 False를 출력
"""

grid = [
  [0, 1, 0, 0],
  [0, 1, 1, 1],
  [0, 0, 0, 1],
  [1, 1, 0, 0]
]

# True
h = len(grid)
w = len(grid[0])

xx = [-1,1,0,0]
yy = [0,0,-1,1]

checked = [[False] * w for _ in range(h)]
roots = []
res = False


def dfs(x,y):
    checked[x][y] = True
    root.append((x,y))
    for k in range(4):
        nx ,ny = x + xx[k] , y + yy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == 0 and not checked[nx][ny]:                
                dfs(nx,ny)


for i in range(h):
    for j in range(w):
        if grid[i][j] == 0 and not checked[i][j]:
            root = []
            dfs(i,j)
            roots.append(root)

if (0,0) == roots[0][0] and (h-1, w-1) == roots[0][-1]:
    res = True
print(res)

##################################################


def dfs(x, y):
    if x == h - 1 and y == w - 1:
        return True
    checked[x][y] = True

    for k in range(4):
        nx, ny = x + xx[k], y + yy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == 0 and not checked[nx][ny]:
                if dfs(nx, ny):
                    return True
    return False

if grid[0][0] == 0:
    res = dfs(0, 0)
else:
    res = False

print(res)
