"""
 *packageName    : 
 * fileName       : 16985.Maaaaaaaaaze
 * author         : ipeac
 * date           : 2023-03-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-01        ipeac       최초 생성
"""
from itertools import permutations

graph = [
    [
        list(map(int, input().split()))
        for _ in range(5)
    ]
    for _ in range(5)
]

def in_range(x, y, z):
    return 0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5

print(f"graph  ==> {graph}")

for combi in permutations(range(5)):
    maze = []
    print(f"combi  ==> {combi}")
    for num in combi:
        maze.append(graph[num])
    print(f"maze  ==> {maze}")
