
n,a = 5 , [6,6,6,6,6,6]
n,a = 100000 , [100001] * 100000
n,a = 5, [3, 4, 4, 6, 1, 4, 4]
n,a = 1 ,[1,2,1]
n,a = 3 , [1,2,3,4]

def solution(N, A):
    counter = [0] * N
    last_max = 0
    current_max = 0

    for i in A:
        if i <= N:
            if counter[i-1] < last_max:
                counter[i-1] = last_max  
            counter[i-1] += 1
            if counter[i-1] > current_max:
                current_max = counter[i-1]
        else:
            last_max = current_max

    for i,v in enumerate(counter):
        if v < last_max:
            counter[i] = last_max
    return counter
print(solution(N=n,A=a))