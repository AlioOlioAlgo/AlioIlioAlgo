"""
 *packageName    :
 * fileName       : 벽이 있는 충돌 실험
 * author         : ipeac
 * date           : 2023-01-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-23        ipeac       최초 생성
 """
t = int(input())  # 테스트 케이스

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def simulate():
    n, m = map(int, input().split())
    way = []
    count_graph = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    way = [
        list(map(str, input().split()))
        for _ in range(n)
    ]
    
    print(f"way = {way}")

for _ in range(t):
    simulate()
