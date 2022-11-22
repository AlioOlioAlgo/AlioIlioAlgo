"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-22        ipeac       최초 생성
 """
import heapq

n, k = map(int, input().split())  # 보석 개수 ,  k 가방에 들어가는 보석
jews = [
    list(map(int, input().split()))
    for _ in range(n)
]
bags = [
    int(input())
    for _ in range(k)
]

jews.sort()
bags.sort()

print(f"jews = {jews}")
print(f"bags = {bags}")

temp = []

for bag in bags:
    print("==========================================")
    while jews and bag >= jews[0][0]:  # 보석의 값이 가방 안인 경우
        heapq.heappush(temp, -jews[0][1])
        heapq.heappop(jews)
        print(f"temp = {temp}")
        print(f"jews = {jews}")
        pass
