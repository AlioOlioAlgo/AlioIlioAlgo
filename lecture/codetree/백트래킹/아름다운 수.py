"""
 *packageName    :
 * fileName       : 아름다운 수
 * author         : ipeac
 * date           : 2023-01-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-25        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
n = int(input())
global_cnt = 0
ans = []

def solution(cnt):
    global global_cnt
    if cnt == n:
        global_cnt += 1
        return
    elif cnt > n:
        return
    else:
        for i in range(1, 5):
            for k in range(i):
                ans.append(i)
            solution(cnt + i)
            
            for k in range(i):
                ans.pop()

solution(0)
print(global_cnt)
