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
def move_wheel():
    pass

for num, dir in wheels:
    print(f"num,dir  ==> {num, dir}")
