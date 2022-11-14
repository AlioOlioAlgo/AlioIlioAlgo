"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-12        ipeac       최초 생성
 """
from collections import deque
from itertools import combinations

n = int(input())
people = list(map(int, input().split()))
sum_people = sum(people)
graph = [
    list(map(int, input().split()))[1:]
    for _ in range(n)
]

def check(combi):
    print("==========================================")
    print(f"combi = {combi}")
    value = combi[0]
    print(f"value = {value}")
    visited = [0 for _ in range(n + 1)]
    q = deque()
    q.append(value)
    visited[value] = 1
    while q:
        x = q.popleft()
        print(f"x = {x}")
        print(f"graph = {graph[x - 1]}")
        for v in graph[x - 1]:
            print(f"v = {v}")
            print(f"visited = {visited}")
            print(f"combi = {combi}")
            if not visited[v] and v in combi:
                q.append(v)
                print(f"q = {q}")
                visited[v] = 1
    print(f"visited = {visited}")
    for c in combi:
        if not visited[c]:
            print('false')
            return False
    print('true')
    return True

min_diff = int(1e9)
arr = set(i for i in range(1, n + 1))
for i in range(1, n // 2 + 1):
    for combi in combinations(arr, i):
        ano_combi = arr - set(combi)
        ano_combi = list(ano_combi)
        if not check(combi) or not check(ano_combi):
            continue
        tmp = 0
        for c in combi:
            tmp += people[c - 1]
        diff_tmp = sum_people - tmp
        if min_diff > abs(tmp - diff_tmp):
            min_diff = abs(tmp - diff_tmp)
if min_diff == int(1e9):
    print(-1)
else:
    print(min_diff)
