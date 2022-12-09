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
n, m = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

choose = [
    [],  # 0
    [[0], [1], [2], [3]],  # 1
    [[0, 2], [1, 3]],  # 2
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4
]

def dfs(graph, cnt):
    global ans
    tmp = [item[:] for item in graph]  # 2차원 배열의 깊은 복사
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    
    y, x, cctv = q[cnt]
    print(f"q[cnt] = {q[cnt]}")
    for i in choose[cctv]:
        pass

graph = []
cctv_cnt = 0
q = []
ans = int(1e9)
for i in range(n):
    input_data = list(map(int, input().split()))
    graph.append(input_data)
    for j in range(len(input_data)):
        if input_data[j] in [1, 2, 3, 4, 5]:  # cctv에 해당하는 번호면 해당 번호와 인덱스를 담아서 저장한다.
            cctv_cnt += 1
            q.append([input_data[j], i, j])
    
    pass

dfs(graph, 0)
