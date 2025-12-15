a = '{[()()]}'

def solution(A):
    stack = []
    table = {
        "]" : "[" ,
        "}" : "{" ,
        ")" : "(" 
    }
    values = table.values()
    for i in A:
        if i in values:
            stack.append(i)
        else:
            if not stack:
                return 0
            else:
                if stack.pop() != table.get(i):
                    return 0   
    if stack:
        return 0
    return 1
print(solution(A=a))