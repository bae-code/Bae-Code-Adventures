m, n = map(int, input().split())
sticks = list(map(int,input().split()))

start = 1
end = max(sticks)

answer = 0

def cut(cut_lan,m):
    cnt = 0
    for stick in sticks:
        cnt += stick // cut_lan
    return cnt >= m 


while start <= end:    
    mid = (start + end) // 2
    if cut(mid,m):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        

print(answer)