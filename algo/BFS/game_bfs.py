from collections import deque
xx = [-1,1,0,0]
yy = [0,0,-1,1]

def bfs(x,y,graph,x_len,y_len):
    
    queue = deque()

    # 최초 좌표를 큐에 저장
    queue.append((x,y))

    while queue:
        #CURRENT_X, CURRENT_Y 현재 좌표
        cx, cy = queue.popleft()
        for d in range(4):
            # 상하좌우 이동 
            nx , ny = cx + xx[d] , cy + yy[d]
            # NX,NY 이동한 좌표
            # 0 <= NX < X_LEN : 벽이아니고, 맵을 넘어가지않음, 처음가는곳임
            if 0 <= nx < x_len and 0 <= ny < y_len and  graph[ny][nx] == 1:
                # 밟은곳은 1을 더해 방문 여부 체크
                graph[ny][nx] = graph[cy][cx] + 1
                # 현재 좌표를 큐에 저장
                queue.append((nx,ny))

def solution(maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]):

    x_len = len(maps[0])
    y_len = len(maps)

    bfs(x=0,y=0,graph=maps,x_len=x_len,y_len=y_len)

    answer = maps[y_len-1][x_len-1]
    if answer == 1:
        return -1
    return answer


print(solution())
print(solution(maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))