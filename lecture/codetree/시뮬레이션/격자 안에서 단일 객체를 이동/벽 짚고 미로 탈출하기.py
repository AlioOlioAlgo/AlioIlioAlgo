"""
 *packageName    :
 * fileName       : 벽 짚고 미로 탈출하기
 * author         : ipeac
 * date           : 2023-01-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-15        ipeac       최초 생성
 """
n = int(input())
x, y = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
