"""
 *packageName    : 
 * fileName       : 20230218
 * author         : ipeac
 * date           : 2023-02-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-18        ipeac       최초 생성
"""
n, l = map(int, input().split())  # n 그래프 길이  l 경사로 길이

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
print(f"graph  ==> {graph}")

def in_range(num):
    return 0 <= num < n

def check_way(way):
    length = len(way)
    visited = [False] * length
    for i in range(length - 1):
        if abs(way[i] - way[i + 1]) > 1:  # 높이 차이가 2이상인 경우 걍 안되는 친구임.
            return False
        
        # 내리막길 고려
        if way[i] - way[i + 1] == 1:
            for j in range(1, l + 1):  # j 1 2
                if not in_range(i + j) or way[i + 1] != way[i + j] or visited[i + j]:
                    return False
                visited[i + j] = True
        # 오르막길 고려
        if way[i + 1] - way[i] == 1:
            for j in range(l):
                if not in_range(i - j) or way[i] != way[i - j] or visited[i - j]:
                    return False
                visited[i - j] = True
    return True

ans = 0
for i in range(n):
    if check_way(graph[i]):
        ans += 1
for j in range(n):
    arr = [graph[i][j] for i in range(n)]
    if check_way(arr):
        ans += 1
print(ans)
