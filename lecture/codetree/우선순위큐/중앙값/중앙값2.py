"""
 *packageName    :
 * fileName       : 중앙값2
 * author         : ipeac
 * date           : 2022-12-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-27        ipeac       최초 생성
 """
import heapq

t = int(input())
for _ in range(t):
    # 테스트 케이스 별 진행
    m = int(input())  # 수열의 크기
    # 수열의 원소가 m 크기만큼 등장합니다.
    arr = list(map(int, input().split()))
    median = arr[0]
    print(median, end=" ")
    min_pq = []
    max_pq = []
    for i in range(1, m):
        # 1번 수열은 짝수임 !
        if i % 2 == 1:  # 짝수 수열인 경우 -> 중앙값보다 크다면 min_pq || 작다면 max_pq 에 담습니다.
            if arr[i] > median:
                heapq.heappush(min_pq, arr[i])
            else:
                heapq.heappush(max_pq, -arr[i])
        else:  # 홀수 수열인 경우 -> min_pq | max_pq 의 크기를 비교후 더 큰 쪽에 있는 친구의 min 혹은 max 값을 중앙값으로 설정
            # 중앙값 기준으로 다시 담습니다.
            if len(min_pq) > len(max_pq):
                cand = heapq.heappop(min_pq)
            else:
                cand = -heapq.heappop(max_pq)
            num = sorted([median, cand, arr[i]])
            # 작은수 중앙값 큰수
            heapq.heappush(max_pq, -num[0])
            median = num[1]
            heapq.heappush(min_pq, num[2])
            print(median, end=" ")
    print()
