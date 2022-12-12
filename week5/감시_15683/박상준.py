"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-09        ipeac       최초 생성
 """
import pprint

n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv_direction = [
    [],  # 0
    [[0], [1], [2], [3]],  # 1
    [[0, 2], [1, 3]],  # 2
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4
    [[0, 1, 2, 3]],  # 5
]

ans = int(1e9)

cctv = []

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

print(f"graph = {graph}")

for i in range(n):
    for j in range(m):
        # print(f"graph[i][j] = {graph[i][j]}")
        if 1 <= graph[i][j] <= 5:  # 그래프1 2 3 4 5 에 해당하는 cctv가 존재한다면
            cctv.append([i, j, graph[i][j]])  # cctv에 해당 cctv의 위치와 어떤 종류의 cctv가 존재하는지 표기한다.
print(f"cctv = {cctv}")

ans = int(1e9)

def check_zero(graph):
    # print("===================제로 체크=======================")
    # print()
    pprint.pprint(graph, width=40)
    zero_cnt = 0
    for item in graph:
        zero_cnt += item.count(0)
    # print(f"zero_cnt = {zero_cnt}")
    return zero_cnt

def dfs(graph, cnt):
    global ans
    if cnt == len(cctv):
        ans = min(ans, check_zero(graph))  # 0 의 개수를 카운트 한다.
        return
    
    x, y, kind = cctv[cnt]
    
    for direction in cctv_direction[kind]:  # choose 2차원 배열 cctv_direction[kind] > [[0, 1], [1, 2], [2, 3], [3, 0]] > direction [0, 1]
        print("====================방향 종류======================")
        print(f"direction = {direction}")
        copyed_graph = [item[:] for item in graph]  # 다음 dfs로 그래프 값을 전달해주기 위함임
        for dir in direction:  # 2차원 배열안의 dir 0 ... 1
            print("====================하나의 cctv에서 각도 돌리는중======================")
            print(f"dir = {dir}")
            nx, ny = cctv[cnt][0:2]
            while True:
                nx, ny = nx + dx[dir], ny + dy[dir]  # 한방향으로 쭉 탐색해야하기에 nx, ny 를 계속 이어서 기산한다.
                print(f"nx, ny = {nx, ny}")
                if 0 <= nx < n and 0 <= ny < m:
                    if copyed_graph[nx][ny] == 6:  # 벽을 만나는 경우 종료
                        break
                    elif copyed_graph[nx][ny] == 0:  # 빈 공간의 경우 '#''을 채워준다.
                        copyed_graph[nx][ny] = '#'
                
                else:
                    break
            print("=====================다돌고 나서의 그래프 모양=====================")
            print(f"copyed_graph = {copyed_graph}")
        dfs(copyed_graph, cnt + 1)

dfs(graph, 0)
print(ans)
