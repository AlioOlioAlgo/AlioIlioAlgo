"""
 *packageName    :
 * fileName       : 중앙값
 * author         : ipeac
 * date           : 2022-12-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-26        ipeac       최초 생성
 """
import heapq

# 변수 선언 및 입력:
t = int(input())
arr = []

def find_median():
    # 중앙값(median)을 계속 관리해줍니다.
    # 중앙값보다 작은 숫자들을 max heap으로 관리하며 (max_pq)
    # 중앙값보다 큰 숫자들을 min heap으로 관리하여 (min_pq)
    # 새로운 숫자가 추가될 때마다
    # 그에 따라 median, max_pq, min_pq를 업데이트 해주면 됩니다.
    median = arr[0]
    max_pq, min_pq = [], []
    print(median, end=" ")
    
    for i in range(1, m):
        # Case 1.
        # 짝수 번째에 새로운 숫자가 주어졌을 경우에는
        # 양쪽 max_pq, min_pq에 들어있는 원소의 수가
        # 정확히 동일할 것이므로
        # 중앙값은 그대로 두고
        # median과 arr[i]값을 비교하여
        # arr[i] < median이라면 max_pq에
        # arr[i] > median이라면 min_pq에 넣어줍니다.
        if i % 2 == 1:
            if arr[i] < median:
                heapq.heappush(max_pq, -arr[i])
            else:
                heapq.heappush(min_pq, arr[i])
        
        # Case 2.
        # 홀수 번째에 새로운 숫자가 주어졌을 경우에는
        # max_pq, min_pq 중 개수가 1개 더 많은 곳이
        # 어디인지에 따라 다른 전략을 취해줍니다.
        else:
            # Step 1.
            # 먼저 max_pq, min_pq 중 개수가 1개 더 많은 쪽에
            # 있는 곳에서 우선순위가 가장 큰 값을 뽑아줍니다.
            # 이를 new_cand라 하겠습니다.
            if len(max_pq) > len(min_pq):
                new_cand = -heapq.heappop(max_pq)
            else:
                new_cand = heapq.heappop(min_pq)
            
            # Step 2.
            # 이제 max_pq, min_pq에 들어있는 숫자의 개수는 정확히
            # 동일할 것입니다.
            # 여기서 우리가 해야 할 일은
            # median, arr[i], new_cand에서
            # 가장 작은 값은 max_pq에
            # 가운데 값은 median에 다시 넣어주고
            # 가장 큰 값은 min_pq에 넣어줘야 하는 것입니다.
            # 이를 정렬을 이용하면 편하게 구현이 가능합니다.
            nums = sorted([median, arr[i], new_cand])
            
            # 순서대로 값을 넣어줍니다.
            heapq.heappush(max_pq, -nums[0])
            median = nums[1]
            heapq.heappush(min_pq, nums[2])
            
            # 홀수 번째의 경우에는 중앙값을 출력해줍니다.
            print(median, end=" ")
    
    print()

for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    
    # 홀수 번째마다 중앙값을 찾는 것을 반복합니다.
    find_median()
