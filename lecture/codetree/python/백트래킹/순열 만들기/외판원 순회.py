"""
 *packageName    : 
 * fileName       : 외판원 순회
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
# n = 4
# graph = [[0, 2, 5, 9], [3, 0, 8, 11], [7, 3, 0, 10], [9, 5, 7, 0]]
print(f"n  ==> {n}")
print(f"graph  ==> {graph}")
min_value = 1e9
visited = [False for _ in range(n)]
moving = []

def calc():
    value = 0
    for i in range(len(moving) - 1):
        value += graph[moving[i]][moving[i + 1]]
    # 1로 가는 경로 계산
    value += graph[moving[-1]][0]
    
    return value

def circulation(cnt):
    global min_value
    if cnt == n and graph[moving[-1]][0] != 0:
        print(f"moving  ==> {moving}")
        print(f"calc()  ==> {calc()}")
        min_value = min(min_value, calc())
        return
    # 몇번째로 이동할건지
    for i in range(n):
        if visited[i]:  # 이미 방문된 곳을 방문하면 안됨.
            continue
        visited[i] = True
        moving.append(i)  # i 번쨰로 이동합니다.
        if graph[moving[-2]][moving[-1]] != 0:
            circulation(cnt + 1)
        moving.pop()
        visited[i] = False

# 1번 시작
visited[0] = True
moving.append(0)
circulation(1)
print(min_value)
