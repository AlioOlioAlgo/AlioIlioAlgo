"""
 *packageName    : 
 * fileName       : 3190.뱀
 * author         : ipeac
 * date           : 2023-03-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-10        ipeac       최초 생성
"""
n = int(input())  # 보드의 크기  N
graph = [
    [0 for _ in range(5)]
    for _ in range(5)
]
move = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북 동 남 서
k = int(input())  # 사과의 개수 K
apples = [
    list(map(int, input().split()))  # 사과의 행 열 (1행 1열에는 사과가 없음)
    for _ in range(k)
]
for x, y in apples:
    graph[x - 1][y - 1] = 1
print(f"graph  ==> {graph}")
l = int(input())  # 뱀의 방향변환 횟수
snakes = [
    list(map(str, input().split()))  # 정수 X , 정수 C
    # 게임시작 시간으로부터 X초가 끝난 뒤에 왼쪽 C 가 'L' 오른쪽 C 가 'D' 로 90도 방향 회전
    for _ in range(l)
]
print(f"snakes  ==> {snakes}")
# 처음에 뱀은 오른쪽을 향합니다.
direction = 1  # 오른쪽

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y, direction):
    nx, ny = x + move[direction][0], y + move[direction][1]
    if in_range(nx,ny) and
    
    pass
