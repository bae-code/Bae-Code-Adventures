a = [-100, -100, 1, 2, 3]
def solution(A):
    # Implement your solution here
    sorted_list = sorted(A, reverse=True)
    max_val = sorted_list[0] * sorted_list[1] * sorted_list[2]
    other_max = sorted_list[0] * sorted_list[-1] * sorted_list[-2]
    return max( max_val, other_max )

print(solution(A=a))