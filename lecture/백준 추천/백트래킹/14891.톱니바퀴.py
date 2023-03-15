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
    another_wheel = [value[:] for value in graph]
    
    switch = dir
    if switch == 1:
        switch = -1
    else:
        switch = 1
    for i in range(num, -1, -1):
        if i != 0:
            connected = False if graph[i][-2] == graph[i - 1][2] else True
            if not connected:
                break
        if i != num:
            
            if switch == -1:  # 반시계
                first = another_wheel[i].pop(0)
                another_wheel[i].append(first)
                switch = 1
            else:  # 시계방향
                last = another_wheel[i].pop()
                another_wheel[i].insert(0, last)
                switch = -1
    
    switch = dir
    
    for i in range(num, 4):
        if i != 3:
            connected = False if graph[i][2] == graph[i + 1][-2] else True
            if not connected:
                break
        if switch == -1:  # 반시계
            switch = 1
            first = another_wheel[i].pop(0)
            another_wheel[i].append(first)
        else:  # dir == 1 # 시계
            switch = -1
            last = another_wheel[i].pop()
            another_wheel[i].insert(0, last)
    graph = [num[:] for num in another_wheel]

for num, dir in wheels:
    print(f"num,dir  ==> {num, dir}")
    move_wheel(num - 1, dir)
    print(f"graph  ==> {graph}")
ans = 0
for i in range(4):
    if graph[i][0] == 1:
        ans += 2 ** i
print(ans)
