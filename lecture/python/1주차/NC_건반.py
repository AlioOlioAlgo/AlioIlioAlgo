"""
 *packageName    :
 * fileName       : NC_건반
 * author         : ipeac
 * date           : 2022-11-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-21        ipeac       최초 생성
 """

black = {2, 4, 6, 9, 11}
white = {1, 3, 5, 7, 8, 10, 12}

def solution(music):
    dis = 0
    # 첫 값 저장
    start = 1
    for i in range(len(music)):
        target = music[i]
        if start > target:
            start, target = target, start
            # print(f"start = {start}")
            # print(f"target = {target}")
        # 중복하지 않고 앞뒤 이동
        for j in range(start, target):
            if j not in black:
                dis += 1
        if start > target:
            start, target = target, start
        if start in black:
            dis += 1
        start = music[i]
    print(dis)

# intel = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5], [3, 5], [5, 6], [5, 7], [6, 7], [7, 8], [8, 9], [8, 10], [9, 10], [10, 11], [10, 12], [11, 12]]
#
# def solution(musics):
#     graph = [[] * 13 for _ in range(13)]
#     for inte in intel:
#         graph[inte[0]].append(inte[1])
#         graph[inte[1]].append(inte[0])
#     print(f"graph = {graph}")
#     ans = 0
#
#     def bfs(v, target):
#         print("==========================================")
#         print(f"v,target = {v, target}")
#         visited = [0 for _ in range(13)]
#         q = deque()
#         q.append(v)  # 시작위치
#         visited[v] = 1  # 시작 시점 방문 처리
#         print(f"visited = {visited}")
#         while q:
#             x = q.popleft()  # 2, 3
#             if x == target:
#                 print(f"visited = {visited[x] - 1}")
#                 return visited[x] - 1
#
#             for k in graph[x]:
#                 if not visited[k]:
#                     q.append(k)
#                     visited[k] = visited[x] + 1
#
#             print(f"q = {q}")
#
#     ans += bfs(1, musics[0])
#     for idx in range(len(musics) - 1):
#         ans += bfs(musics[idx], musics[idx + 1])
#     print(ans)
#     return ans
#
solution([10, 9, 4, 5, 12])
solution([6, 4, 2, 11])
