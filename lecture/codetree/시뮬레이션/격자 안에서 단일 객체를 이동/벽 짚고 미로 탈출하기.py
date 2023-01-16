"""
 *packageName    :
 * fileName       : 벽 짚고 미로 탈출하기
 * author         : ipeac
 * date           : 2023-01-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-15        ipeac       최초 생성
 """
n = int(input())
x, y = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 그래프안에 위치한지 체크
def in_graph(x, y):
    return 0 < x <= n and 0 < y <= n

# 바라보고 있는 방향으로 이동하는 것이 가능한 경우
# 바로 앞이 격자 밖이라면 이동하여 탈출합니다.

def avaliable_forward_out_graph(x, y):
    pass
#
# 해당 방향으로 이동했다 가정시 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다면, 그 방향으로 한칸 이동
