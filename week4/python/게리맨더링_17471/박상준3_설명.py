"""
 *packageName    :
 * fileName       : 게리멘더링
 * author         : ipeac
 * date           : 2022-12-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-03        ipeac       최초 생성
 """
from collections import deque
from itertools import combinations

n = int(input())  # n  구역의 개수
arr = [i for i in range(1, n + 1)]  # 구역은 1번부터 6까지가
print(f"arr = {arr}")
#  인구가 1번 구역부터 N번 구역까지 순서대로 주어진다
people = list(map(int, input().split()))
sum_people = sum(people)  # 총 인구수
# 각 구역과 인접한 구역의 번호
graph = [
    list(map(int, input().split()))[1:]
    for _ in range(n)
]

def check(combi):  # 이 함수는 매개변수로 받은 set이 서로서로 연결되어있는지를 확인하는 함수이다.
    print("===================checkehck=======================")
    print(f"combi = {combi}")
    visited = [0 for _ in range(n + 1)]
    visited[combi[0]] = 1  # 처음 방문한 곳 방문 처리
    print(f"visited = {visited}")
    
    q = deque()  # 첫 순회값
    q.append(combi[0])
    while q:
        x = q.popleft()
        print(f"graph[x - 1] = {graph[x - 1]}")
        print(f"x = {x}")
        for v in graph[x - 1]:
            print(f"visited[v] = {visited[v]}")
            if not visited[v] and v in combi:  # 방문하지 않은 곳이며 해당 값이 combi 안에 있는 값이라면 순회를 한다.
                q.append(v)
                visited[v] = 1
    # 여기서 combi 값이 전부 방문되었는지 체크한다.
    for c in combi:
        if not visited[c]:
            print('false')
            return False
    return True

print(f"graph = {graph}")
min_value = int(1e9)

# 일단 구역이 6개라면 1 2 3  || 4 5  6 으로 나뉘어 있을 수도 있고, 1 || 2 3 4 5 6 으로 나뉘어 있을 수도 있다. 모든 나뉜 경우의 수를 고려해야한다.
for repeat in range(1, n // 2 + 1):  # 다 돌 필요는 없고 절반만 돌아도 모든 경우의 수를 고려할 수 있다.
    for combi in combinations(arr, repeat):  # 1개 부터 총 n 개 까지의 조합을 만들어서 경우의 수를 고려한다.
        print("==========================================")
        combi_set = set(combi)
        another_combi = set(arr) - combi_set
        another_combi = list(another_combi)
        # print(f"another_combi = {another_combi}")
        # print(f"combi = {combi}")
        if not check(combi) or not check(another_combi):  # 해당 콤비가 하나라도 순회가 불가능 하다면 연산할 가치조차 없다.
            continue
        
        # 해당 콤바가 전부 순회 가능하다면 해당 인구 사이의 차이값이 이전 인구 값보다 작다면 변수를 담는다.
        tmp = 0
        
        # 일단 하나구역의 인구만 구해도 나머지 인구를 유추할 수 있다.
        for c in combi:
            tmp += people[c - 1]
        another_tmp = sum_people - tmp
        min_value = min(min_value, abs(another_tmp - tmp))
if min_value == int(1e9):
    print(-1)
    exit()

print(min_value)
