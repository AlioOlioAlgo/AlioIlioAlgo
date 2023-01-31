"""
 *packageName    :
 * fileName       : 1차원 윷놀이
 * author         : ipeac
 * date           : 2023-01-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-30        ipeac       최초 생성
 """

n, m, k = map(int, input().split())  # n번의 턴 숫자 주어짐 || 하나의 말을 선택하여 m 도착시 1점 || k 개의 말
n_list = list(map(int, input().split()))
horses = [1 for _ in range(k)]
max_score = 0

def calc():
    score = 0
    for horse in horses:
        score += (horse >= m)
    
    return score

def move(cnt):
    global max_score
    if cnt == n:
        return
    
    for i in range(k):
        if horses[i] >= m:
            continue
        
        horses[i] += n_list[cnt]
        move(cnt + 1)
        horses[i] -= n_list[cnt]

move(0)
print(max_score)
