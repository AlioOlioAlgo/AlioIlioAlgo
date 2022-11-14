"""
 *packageName    :
 * fileName       : 박상준4
 * author         : ipeac
 * date           : 2022-11-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-14        ipeac       최초 생성
 """
n, m, h = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(h + 1)]
ans = int(1e9)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[a][b + 1] = -1
if m == 0:
    print(0)
    exit()

# print(f"graph = {graph}")

def check():
    # print("======check====================================")
    # pprint.pprint(graph)
    for col in range(1, n + 1):
        start = col
        for row in range(1, h + 1):
            # print(f"row,start = {row, start}")
            if graph[row][start] == 1:  # 오른쪽이 1인 경우
                start += 1
            elif graph[row][start] == -1:
                start -= 1
            # print(f"start = {start}")
        if start != col:
            # print(f"start = {start}")
            # print(f"col = {col}")
            return False
    # print('트루')
    return True

def make_line(x, y, cnt):
    global ans
    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return
    # print("==========================================")
    # print(f"x, y = {x, y}")
    for row in range(x, h + 1):
        for col in range(y, n):
            if not graph[row][col] and not graph[row][col + 1]:
                # print(f"row,col = {row, col}")
                graph[row][col] = 1
                graph[row][col + 1] = -1
                make_line(row, col + 2, cnt + 1)  # 적어도 두칸은 떨어져야함
                graph[row][col] = 0
                graph[row][col + 1] = 0
        y = 0

make_line(1, 1, 0)

if ans == int(1e9):
    print(-1)
    exit()

print(-1 if ans > 3 else ans)
