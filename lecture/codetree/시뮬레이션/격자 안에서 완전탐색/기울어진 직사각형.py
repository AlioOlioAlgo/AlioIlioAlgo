"""
 *packageName    :
 * fileName       : 기울어진 직사각형
 * author         : ipeac
 * date           : 2022-12-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-30        ipeac       최초 생성
 """
n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
ans = 0

def in_range(x, y):  # 안에 들어가있다면 true를 반환한다.
    return 0 <= x < n and 0 <= y < n

def get_score(x, y, k, l):
    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    move_nums = [k, l, k, l]
    
    sum_of_nums = 0
    
    # 기울어진 직사각형의 경계를 따라간다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        print(f"dx,dy,move_num = {dx, dy, move_num}")
        for _ in range(move_num):
            x, y = x + dx, y + dy
            
            # 기울어진 직사각형이 경계를 벗어나느 경우면
            # 불가능하다는 의미로 답이 갱신되지 않도록
            # 0을 반환한다.
            if not in_range(x, y):
                return 0
            print(f"x, y  ==> {x, y}")
            print(f"graph[x][y]  ==> {graph[x][y]}")
            sum_of_nums += graph[x][y]
    
    return sum_of_nums

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                print("==========================================")
                print(f"i,j,k,l = {i, j, k, l}")
                ans = max(ans, get_score(i, j, k, l))
print(ans)
