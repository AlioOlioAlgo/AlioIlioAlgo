"""
 *packageName    : 
 * fileName       : 기울어진 직사각형2
 * author         : ipeac
 * date           : 2023-02-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-24        ipeac       최초 생성
"""
n = int(input())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

print(f"graph  ==> {graph}")
