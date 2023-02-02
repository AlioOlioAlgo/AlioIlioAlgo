"""
 *packageName    :
 * fileName       : 단순한 동전 챙기기
 * author         : ipeac
 * date           : 2023-02-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-02        ipeac       최초 생성
 """
n = int(input())
graph = [
    list(map(int, input()))
    for _ in range(n)
]
print(f"graph = {graph}")
