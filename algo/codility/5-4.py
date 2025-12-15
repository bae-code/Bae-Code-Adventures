exam = [4, 2, 2, 5, 1, 5, 8]

def solution(A):
    min_avg = float('inf')
    res_idx = 0
    # [수정 1] N-1까지 돌아야 마지막 두 개(A[N-2], A[N-1])를 체크함
    for i in range(len(A) - 1):
        
        # 1. 길이 2짜리 검사 (무조건 가능)
        val_2 = (A[i] + A[i+1]) / 2.0
        if val_2 < min_avg:
            min_avg = val_2
            res_idx = i
            
        # 2. 길이 3짜리 검사 (인덱스가 허용될 때만)
        if i < len(A) - 2:
            val_3 = (A[i] + A[i+1] + A[i+2]) / 3.0
            if val_3 < min_avg:
                min_avg = val_3
                res_idx = i # [중요] 평균 같으면 앞쪽 인덱스 유지해야 하므로 < 사용 (<= 아님)
                
    return res_idx

solution(A=exam)