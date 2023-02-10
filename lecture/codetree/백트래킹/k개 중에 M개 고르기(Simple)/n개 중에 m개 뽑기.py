"""
 *packageName    :
 * fileName       : n개 중에 m개 뽑기
 * author         : ipeac
 * date           : 2023-02-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-01        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

n_list = []

def print_answer():
    print(*n_list)

def make_list(curr_num, cnt):
    if cnt == m:
        print_answer()
        return
    
    for i in range(curr_num, n + 1):
        n_list.append(i)
        make_list(i + 1, cnt + 1)
        n_list.pop()

make_list(1, 0)
