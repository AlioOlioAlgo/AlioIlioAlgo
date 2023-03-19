"""
 *packageName    : 
 * fileName       : 14891.톱니바퀴
 * author         : ipeac
 * date           : 2023-03-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-15        ipeac       최초 생성
 """
graph = [
    list(map(int, input()))
    for _ in range(4)
]
print(f"graph  ==> {graph}")
cnt = int(input())
wheels = [
    list(map(int, input().split()))
    for _ in range(cnt)
]
print(f"wheels  ==> {wheels}")

# 12 시 방향부터 나란히 나열 되어있다.
# 방향 1 시계방향 1칸 || 방향 0 반시계방향 1칸
#
# 톱니바퀴를 돌립니다.
# dir == 1 이면 오른쪽으로 밀고 dir == -1 이면 왼쪽으로 밀어야합니다.
def move_wheel(num, dir):
    global graph
    move = [0] * 4
    move[num] = dir  # 초기 톱니바퀴의 움직임 설정
    
    # 왼쪽 톱니 움직임 확인
    for i in range(num - 1, -1, -1):
        if graph[i][2] != graph[i + 1][-2]:
            move[i] = -move[i + 1]
        else:
            break
    # 오른쪽 톱니 움직임 확인
    for i in range(num + 1, 4):
        if graph[i][-2] != graph[i - 1][2]:
            move[i] = -move[i - 1]
        else:
            break
    print(f"move  ==> {move}")
    # 각 톱니바퀴의 움직임에 따라 톱니바퀴 회전
    for i in range(4):
        if move[i] == 1:
            last = graph[i].pop()
            graph[i].insert(0, last)
        elif move[i] == -1:
            first = graph[i].pop(0)
            graph[i].append(first)

for num, dir in wheels:
    print(f"num,dir  ==> {num, dir}")
    move_wheel(num - 1, dir)
    print(f"graph  ==> {graph}")
ans = 0
for i in range(4):
    if graph[i][0] == 1:
        ans += 2 ** i
print(ans)
