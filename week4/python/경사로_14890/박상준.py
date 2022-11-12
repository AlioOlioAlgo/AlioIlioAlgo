"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-12        ipeac       최초 생성
 """
n, l = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
result = 0

def pos(now):
    for i in range(1, n):
        if abs(now[i] - now[i - 1]) > 1:  # 양 그래프의 차이가 1 초과라면 오르내릴수 없기에 false처리
            return False
        if now[i] > now[i - 1]:  # 현재 값이 이전 값보다 크다 ( 오르는 길이다) 작은 쪽 now[i-1]를 기준으로 경사로 가능 여부 체크
            for k in range(l):
                if i - 1 - k < 0 or used[i - 1 - k] or now[i - 1] != now[i - 1 - k]:
                    return False
                if now[i - 1] == now[i - 1 - k]:
                    used[i - 1 - k] = True
        elif now[i] < now[i - 1]:  # 이전 값이 현재 값보다 크다 ( 내리는 길이다) 작은 쪽 now[i] 를 기준으로 경사로 가능 여부를 체크한다.
            for k in range(l):
                if i + k >= n or used[i + k] or now[i] != now[i + k]:
                    return False
                if now[i] == now[i + k]:
                    used[i + k] = True
    return True

# 가로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if pos(graph[i]):
        result += 1
# 세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):
        result += 1
print(result)
