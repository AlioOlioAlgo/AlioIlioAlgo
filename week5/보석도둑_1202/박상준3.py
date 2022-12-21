"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-12-13
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-13        ipeac       최초 생성
 """
import heapq
import sys
import time

start = time.time()

input = sys.stdin.readline

n, k = map(int, input().split())
jew_info = [
    list(map(int, input().split()))  # 무게 || 가격
    for _ in range(n)
]
bag_info = [
    int(input())
    for _ in range(k)
]

jew_info.sort()
bag_info.sort()

ans = 0
temp = []
for bag in bag_info:
    print("==========================================")
    print(f"bag = {bag}")
    while jew_info and bag >= jew_info[0][0]:  # 가방의 최대 무게 이하인 보석들을 담습니다.
        heapq.heappush(temp, -heapq.heappop(jew_info)[1])  # 최대힙 구현을 위해
        print(f"jew_info = {jew_info}")
        print(f"temp = {temp}")
    # pop -> 최댓값 제거됨. 가방에 하나만 넣을 수 있으니. 맨앞에 값넣고 temp 초기..;;?
    # 최소 가방무게를 통과하는 친구들... 이후 가방 무게도 통과할 수 있기에 초기에.
    if temp:
        ans -= heapq.heappop(temp)  # 99 65 이후 한번 더 돌텐데 > 처리..? temp [99]
    elif not jew_info:
        break  # for문 자체가 종료되어버림 모두 빠졌으니...ㅡㅏㅣㅏㅢ
end = time.time()
print(f"{end - start:.5} sec")
print(ans)
