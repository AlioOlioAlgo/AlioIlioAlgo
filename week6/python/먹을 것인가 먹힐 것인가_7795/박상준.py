"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-18        ipeac       최초 생성
 """
t = int(input())

def bisect_left(target, data, start, end):
    if start >= end:
        return start
    mid = start + (end - start) // 2
    if data[mid] < target:
        return bisect_left(target, data, mid + 1, end)
    else:
        return bisect_left(target, data, start, mid)

for _ in range(t):
    n, m = map(int, input().split())  # a 의 수  || b 의 수
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    
    # print(f"a = {a}")
    # print(f"b = {b}")
    ans = 0
    for av in a:
        ans += bisect_left(av, b, 0, len(b))
    print(ans)
