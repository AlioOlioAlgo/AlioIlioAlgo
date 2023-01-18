n = int(input())
x, y = map(lambda x: int(x) - 1, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[[False for _ in range(n)] for __ in range(n)] for ___ in range(4)]  # 각 방향에 대한 visited

def move(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    curr_dir, time = 0, 0
    
    while True:
        # 이미 방문한 곳이면 더 이상 탈출 불가
        if visited[curr_dir][x][y]:
            return -1
        
        # 방문 처리
        visited[curr_dir][x][y] = True
        
        nx = x + dx[curr_dir]
        ny = y + dy[curr_dir]
        
        # 격자 밖으로 탈출이 가능한 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return time + 1
        
        # 바라보고 있는 방향으로 이동하는 것이 가능하지 않은 경우
        if grid[nx][ny] == "#":
            curr_dir = (curr_dir + 3) % 4
        
        # 바라보고 있는 방향으로 이동하는 것이 가능한 경우
        else:
            # 그 위치로 일단 이동
            x, y = nx, ny
            time += 1
            
            # 오른쪽에 짚을 벽이 있는지 체크
            nx = x + dx[(curr_dir + 1) % 4]
            ny = y + dy[(curr_dir + 1) % 4]
            
            # 짚을 벽이 경계밖인 경우도 예외 체크를 해야 하나...???
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            # 오른쪽에 짚을 벽이 없다면...
            if grid[nx][ny] != "#":
                time += 1
                curr_dir = (curr_dir + 1) % 4
                x, y = nx, ny

print(move(x, y))
