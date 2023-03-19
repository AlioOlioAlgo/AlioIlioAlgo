"""
 *packageName    : 
 * fileName       : 수들 중 최솟값 최대화하기
 * author         : ipeac
 * date           : 2023-02-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-11        ipeac       최초 생성
"""
n = int(input())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_value = -1e9
color = []
visited = [False for _ in range(n)]

def calc():
    min_value = 1e9
    for i in range(n):
        print(f"graph  ==> {graph[i][color[i]]}")
        min_value = min(min_value, graph[i][color[i]])
    
    return min_value

def make_color(cnt):
    global max_value
    if cnt == n:
        print(f"color  ==> {color}")
        max_value = max(max_value, calc())
        return
    
    for i in range(n):
        if visited[i]:
            continue
        color.append(i)
        visited[i] = True
        
        make_color(cnt + 1)
        
        color.pop()
        visited[i] = False

make_color(0)
print(max_value)
