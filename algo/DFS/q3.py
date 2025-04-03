"""
0은 빈 칸, 1은 벽으로 구성된 2차원 배열이 주어진다.
연결된 0 덩어리(상하좌우만 연결 가능)가 몇 개인지 구해라.

예시 입력:
grid = [
  [0, 0, 1, 1, 0],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 1, 0, 0]
]

출력: 4
"""

grid = [
  [0, 0, 1, 1, 0],
  [1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 1, 0, 0]
]
h = len(grid)
w = len(grid[0])
visited = [[False]*len(grid[0]) for _ in range(len(grid))]
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0

def solve(x,y):

    visited[x][y] = True
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == 0 and not visited[nx][ny]:
                solve(nx,ny)

                

for i in range(h):
    for j in range(w):
        if grid[i][j] == 0 and not visited[i][j]:
            solve(i,j)
            res += 1

print(res)        
                





