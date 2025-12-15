"""
Docstring for algo.codility.5-3
문제 상황:DNA 염기서열 문자열 S가 주어집니다. (예: "CAGCCTA")각 문자는 "임팩트 계수"라는 숫자를 가집니다.A = 1, C = 2, G = 3, T = 4P와 Q라는 배열이 주어지는데, 이건 **질문(Query)**입니다.질문: "S의 P[i]번째부터 Q[i]번째까지 자른 구간에서, **가장 작은 숫자(최소 임팩트 계수)**는 무엇인가?"예시: S = "CAGCCTA"구간 [2, 4] (GCC) $\rightarrow$ 숫자로 바꾸면 3, 2, 2 $\rightarrow$ 최솟값 2 (C)구간 [0, 5] (CAGCCT) $\rightarrow$ 최솟값 1 (A)
"""
s,p,q = 'CAGCCTA', [2, 5, 0], [4, 5, 6]
def solution(S, P, Q):
    prefix_A = [0] * (len(S) + 1)
    prefix_C = [0] * (len(S) + 1)
    prefix_G = [0] * (len(S) + 1)
    prefix_T = [0] * (len(S) + 1)

    for i, c in enumerate(S):
        prefix_A[i+1] = prefix_A[i]
        prefix_C[i+1] = prefix_C[i]
        prefix_G[i+1] = prefix_G[i]
        prefix_T[i+1] = prefix_T[i]
        if c == "A":
            prefix_A[i+1] += 1
        elif c == 'C':
            prefix_C[i+1] += 1
        elif c == 'G':
            prefix_G[i+1] += 1
        elif c == 'T':
            prefix_T[i+1] += 1

    result = []
    for s_idx, e_idx in zip(P, Q): # s_idx: Start, e_idx: End
        # 구간 내에 A가 있나? (끝점 - 시작점전 > 0)
        print(e_idx+1, s_idx)
        if prefix_A[e_idx+1] - prefix_A[s_idx] > 0:
            result.append(1)
        elif prefix_C[e_idx+1] - prefix_C[s_idx] > 0:
            result.append(2)
        elif prefix_G[e_idx+1] - prefix_G[s_idx] > 0:
            result.append(3)
        else:
            result.append(4) # A,C,G 다 없으면 T
    return result

print(solution(S=s,P=p,Q=q))