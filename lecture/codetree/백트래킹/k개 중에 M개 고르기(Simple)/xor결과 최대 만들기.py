"""
 *packageName    :
 * fileName       : xor결과 최대 만들기
 * author         : ipeac
 * date           : 2023-02-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-01        ipeac       최초 생성
 """
n, m = map(int, input().split())

n_list = list(map(int, input().split()))
choose = []
max_value = -1e9

def xor():
    value = choose[0]
    for idx in range(1, m):
        value ^= choose[idx]
    return value

def choose_all(idx, cnt):
    global max_value
    if cnt == m:
        max_value = max(max_value, xor())
        return
    
    for idx2 in range(idx, n):
        choose.append(n_list[idx2])
        choose_all(idx2 + 1, cnt + 1)
        choose.pop()

choose_all(0, 0)
print(max_value)
