"""
 *packageName    : 
 * fileName       : 수들의 합 최대화하기
 * author         : ipeac
 * date           : 2023-02-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-11        ipeac       최초 생성
"""

# n = 3
# graph = [[3, 5, 3], [5, 8, 4], [2, 7, 1]]
n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False for _ in range(n)]
painted = []

def calc():
    value = 0
    for i in range(n):
        value += graph[i][painted[i]]
    return value

ans = -1e9

def paint(cnt):
    global ans
    if cnt == n:
        print(f"painted  ==> {painted}")
        ans = max(ans, calc())
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        painted.append(i)
        
        paint(cnt + 1)
        
        visited[i] = False
        painted.pop()

paint(0)
print(ans)
