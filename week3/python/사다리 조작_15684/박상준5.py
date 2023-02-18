"""
 *packageName    : 
 * fileName       : 박상준5
 * author         : ipeac
 * date           : 2023-02-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-12        ipeac       최초 생성
"""
import pprint
import sys

n, m, h = map(int, input().split())  # n 세로선의 개수  m 가로선의 개수    h 세로선마다 가로선을 놓을 수 있는 위치
graph = [
    [0 for _ in range(n)]
    for _ in range(h)
]
for i in range(m):
    a, b = map(int, input().split())  # a : 가로 점선  b 번 세로선 과 b+1번 세로선과 연결함
    # 1오른쪽 -1 왼쪽 이동 기준
    graph[a - 1][b - 1] = 1
    graph[a - 1][b] = -1

# 단, 두 가로선이 연속하거나 서로 접하면 안 된다 **
pprint.pprint(graph, width=80)
print("======================================================")
if m == 0:
    print(0)
    sys.exit(0)

ans = 1e9

def check():
    #  i 번 세로선의 결과가 i 번이 나오는지 체크합니다.
    for j in range(n):  # 세로선
        moving = j
        for i in range(h):  # 가로선
            moving += graph[i][moving]
        if moving != j:
            return False
    return True

def place_line(x, y, cnt):
    global ans
    # print(f"cnt  ==> {cnt}")
    # pprint.pprint(graph, width=80)
    if cnt > 3 or ans <= cnt:
        return
    if check():
        # print("======================================================")
        print(f"cnt  ==> {cnt}")
        # pprint.pprint(graph, width=80)
        ans = min(ans, cnt)
        return
    
    if cnt == h:
        return
    
    for xx in range(x, h):
        for yy in range(y, n - 1):
            if graph[xx][yy] == 0 and graph[xx][yy + 1] == 0:
                print(f"xx,yy  ==> {xx, yy}")
                graph[xx][yy] = 1
                graph[xx][yy + 1] = -1
                place_line(xx, yy + 2, cnt + 1)  # i ->x  j -> y
                graph[xx][yy] = 0
                graph[xx][yy + 1] = 0
        y = 0

place_line(0, 0, 0)

if ans > 3:
    print(-1)
else:
    print(ans)
