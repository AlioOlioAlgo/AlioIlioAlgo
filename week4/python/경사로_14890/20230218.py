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
n, l = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
print(f"graph  ==> {graph}")

def in_range(num):
    return 0 <= num < n

# 가로 체크
for i in range(n):
    used = [False for _ in range(n)]
    for j in range(n - 1):
        # 내리는 길인지 오르는 길인지 체크
        # 내리는 길
        if in_range(j) and graph[i][j] > graph[i][j + 1]:  # 3 2 2
            
            pass
        # 오르는 길
        elif in_range(j) and graph[i][j] < graph[i][j + 1]:
            
            pass

# 세로 체크
for i in range(n):
    for j in range(n - 1, -1, -1):  # 아래 위 검사
        
        pass
    for j in range(n):  # 위 아래 검사
        
        pass
