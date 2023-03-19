"""
 *packageName    :
 * fileName       : 행복한 수열의 개수
 * author         : ipeac
 * date           : 2022-12-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-28        ipeac       최초 생성
 """
n, m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

def check_all_right(row, col, direction):
    cnt = 1
    max_cnt = 1
    if direction == "row":
        for i in range(1, n):
            if graph[row][i - 1] == graph[row][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
    
    
    elif direction == "col":
        for i in range(1, n):
            if graph[i - 1][col] == graph[i][col]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
    
    if max_cnt >= m:
        return True
    else:
        return False

ans = 0

# 가로 비교
for row in range(n):
    if check_all_right(row, 0, "row"):
        # 조건 통과시 행복한 수열입니다.
        ans += 1

# 세로 비교
for col in range(n):
    if check_all_right(0, col, "col"):
        ans += 1
print(ans)
