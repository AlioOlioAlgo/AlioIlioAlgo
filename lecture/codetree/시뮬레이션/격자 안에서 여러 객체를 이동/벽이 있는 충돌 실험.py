"""
 *packageName    :
 * fileName       : 벽이 있는 충돌 실험
 * author         : ipeac
 * date           : 2023-01-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-23        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
t = int(input())  # 테스트 케이스

dx = [0, 1, 0, -1]  # 동 남 서 북
dy = [1, 0, -1, 0]

key = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3
}
way = []
count_graph = []

def simulate():
    global way
    global count_graph
    n, m = map(int, input().split())
    
    way = []
    count_graph = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for _ in range(m):
        a, b, c = map(str, input().split())
        way.append([int(a) - 1, int(b) - 1, key[c]])
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def move_one(x, y, dir, idx):
        nx, ny = x + dx[dir], y + dy[dir]
        if in_range(nx, ny):
            way[idx] = [nx, ny, dir]
        else:  # 격자 밖으로 나간다면 그냥 방향만 바꿔줍니다.
            way[idx] = [x, y, (dir + 2) % 4]
    
    def check_marble_count():
        global count_graph
        count_graph = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]
        for w in way:
            count_graph[w[0]][w[1]] += 1
    
    def remove_dup():
        global way
        temp_way = [
        ]
        for w in way:
            if count_graph[w[0]][w[1]] == 1:
                temp_way.append(w)
        way = [num[:] for num in temp_way]
    
    def move():  # 1초 뒤의 마블들의 위치를 계산합니다.
        for k in range(len(way)):
            move_one(way[k][0], way[k][1], way[k][2], k)
        # 구슬 위치 카운트 기록해서 새로운 way로 업데이트가 필요합니다.
        check_marble_count()
        remove_dup()
    
    for i in range(n * 2):  # n *2 크기만큼 반복 횟수 고정
        move()

for _ in range(t):
    simulate()
    print(len(way))
