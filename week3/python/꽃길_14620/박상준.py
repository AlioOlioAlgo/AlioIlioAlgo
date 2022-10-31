"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-31        ipeac       최초 생성
 """
import sys

def check(i, j, visited):
    for idx in range(4):
        ni = i + d[idx][0]
        nj = j + d[idx][1]
        if (ni, nj) in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer: return
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if check(i, j, visited) and (i, j) not in visited:
                    temp = [(i, j)]
                    temp_cost = fields[i][j]
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N = int(input())
answer = int(1e9)
fields = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dfs([], 0)

print(answer)
# https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-14620.-%EA%BD%83%EA%B8%B8-by-Python
