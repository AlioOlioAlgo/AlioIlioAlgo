"""
 *packageName    : 
 * fileName       : 거꾸로 순열
 * author         : ipeac
 * date           : 2023-02-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-09        ipeac       최초 생성
"""
n = int(input())
visited = [False for _ in range(n + 1)]
arr = []

def print_arr():
    for ar in arr:
        print(ar, end=" ")
    print()

def make_permutations(cnt):
    if cnt == n:
        print_arr()
        return
    
    for i in range(n, 0, -1):
        if visited[i]:
            continue
        visited[i] = True
        arr.append(i)
        make_permutations(cnt + 1)
        arr.pop()
        visited[i] = False

make_permutations(0)
