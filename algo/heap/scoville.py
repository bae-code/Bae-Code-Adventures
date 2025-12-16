import heapq
def solution(scoville=[1, 2, 3, 9, 10, 12], K=7):
    answer = 0
    # 이미 존재하는 리스트를 힙으로 만듬
    heapq.heapify(scoville)
    while True:
        # 힙에서 가장 작은값을 뽑아준다
        first_v = heapq.heappop(scoville)
        # 가장 작은 값이 목표치 보다 높거나 같으면 종료
        if first_v >= K:
            break
        # 뽑을 값이없다면 실패
        if len(scoville) == 0:
            return -1
        # 힙에서 가장 작은값을 뽑아준다.
        second_v = heapq.heappop(scoville)

        # 새로운 스코빌을 구한다
        new_sco = first_v + (second_v * 2 )
        # 힙에 새로운 스코빌을 저장한다
        heapq.heappush(scoville,new_sco)
        answer += 1
    
    return answer


print(solution())