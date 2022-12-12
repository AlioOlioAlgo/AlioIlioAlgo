"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-06        ipeac       최초 생성
 """

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

# graph = [[2, 2, 2], [4, 4, 4], [8, 8, 8]]
# print(f"graph = {graph}")

def move(copyed_graph, direction):  # 0 동  1 서   2  북  3  남
    # copyed_graph  복사된 그래프,  direction  이동 방향
    if direction == 0:  # 동쪽으로 그래프를 이동시킨다.
        for row in range(n):
            cursor = n - 1
            for col in range(n - 2, -1, -1):
                if copyed_graph[row][col] != 0:
                    tmp = copyed_graph[row][col]
                    copyed_graph[row][col] = 0
                    if copyed_graph[row][cursor] == 0:
                        copyed_graph[row][cursor] = tmp
                    elif copyed_graph[row][cursor] == tmp:
                        copyed_graph[row][cursor] *= 2
                        cursor -= 1
                    else:
                        cursor -= 1
                        copyed_graph[row][cursor] = tmp
    
    elif direction == 1:  # 서쪽으로 이동시킨다.
        for row in range(n):
            cursor = 0
            for col in range(1, n):
                if copyed_graph[row][col] != 0:  # 0이 아닌 값이라면
                    tmp = copyed_graph[row][col]
                    copyed_graph[row][col] = 0  # 일단 비워질 예정이니.. 0으로 바꾼다
                    if copyed_graph[row][cursor] == 0:  # 왼쪽이 비어있으면 움직이게 해줘야지
                        copyed_graph[row][cursor] = tmp  # 여기서 커서값을 그대로 두는 이유 : 커서 값이 가만히 있어야 값이 이동한 이후 그 다음 숫자가 같으면,, 합차기, 아니면 뒤로 넣기를 할 예정이기 때문이다.
                        pass
                    elif copyed_graph[row][cursor] == tmp:
                        copyed_graph[row][cursor] *= 2  # 왼 오 합치기 2배
                        cursor += 1  # 커서를 이동한다
                    else:  # 비어있지도 않고, 값이 cursor 값과 다르다
                        cursor += 1
                        copyed_graph[row][cursor] = tmp  # 0 1 0 3 2 > 1 0 0 3 2  : 1값 바로 옆에 3을 붙여야 하기 떄문에
    
    elif direction == 2:  # 북쪽으로 배열을 이동시킨다.
        for col in range(n):
            cursor = n - 1
            for row in range(n - 2, -1, -1):
                if copyed_graph[row][col] != 0:  # 0이 아닌값이라면
                    tmp = copyed_graph[row][col]
                    copyed_graph[row][col] = 0  # 일단 비워질 예정이니 .. 0으로 변경한다.
                    if copyed_graph[cursor][col] == 0:  # 커서의 값이 0이라면 tmp값을 올려준다.
                        copyed_graph[cursor][col] = tmp
                    elif copyed_graph[cursor][col] == tmp:
                        copyed_graph[cursor][col] *= 2
                        cursor -= 1
                    else:
                        cursor -= 1
                        copyed_graph[cursor][col] = tmp
    
    elif direction == 3:  # 남쪽으로 배열을 이동시킨다.
        for col in range(n):
            cursor = 0
            for row in range(1, n):
                if copyed_graph[row][col] != 0:  # 0이 아닌 값이 존재한다면
                    tmp = copyed_graph[row][col]
                    copyed_graph[row][col] = 0  # 일단 비워질 예정이니.. 0으로 변경한다.
                    if copyed_graph[cursor][col] == 0:
                        copyed_graph[cursor][col] = tmp
                    elif copyed_graph[cursor][col] == tmp:
                        copyed_graph[cursor][col] *= 2
                        cursor += 1
                    else:
                        cursor += 1
                        copyed_graph[cursor][col] = tmp
        # print(f"copyed_graph = {copyed_graph}")
    
    return copyed_graph

ans = 0

def dfs(graph, cnt):  # 좌 우 상 하 이동 후 합치는 함수입니다. 해당 머지가 좌, 우 , 상  하 어디로 이동되었는지가 중요합니다.
    global ans
    if cnt == 5:
        print(list(map(max, graph)))
        ans = max(ans, max(map(max, graph)))
        # print(f"ans = {ans}")
        return
    for i in range(4):  # 4방향으로 이동한 그래프를 생성한다.
        copyed_graph = [item[:] for item in graph]
        moved_graph = move(copyed_graph, i)
        # print(f"moved_graph = {moved_graph}")
        dfs(moved_graph, cnt + 1)

dfs(graph, 0)
print(ans)
