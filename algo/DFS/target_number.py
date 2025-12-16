

def solution(numbers=[1, 1, 1, 1, 1] , target=3):
    answer = 0
    def dfs(idx, total):
        if idx == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx+1, total + numbers[idx])
        dfs(idx+1, total - numbers[idx])

    dfs(0,0)
    return answer

print(solution())