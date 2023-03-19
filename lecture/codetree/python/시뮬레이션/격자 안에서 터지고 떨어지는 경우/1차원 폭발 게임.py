"""
 *packageName    :
 * fileName       : 1차원 폭발 게임
 * author         : ipeac
 * date           : 2023-01-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-04        ipeac       최초 생성
 """
n, m = map(int, input().split())
boom_list = [
    int(input())
    for _ in range(n)
]
trigger = True

def end_idx_return(start_idx, current_num):
    for end_idx in range(start_idx + 1, len(boom_list)):
        if boom_list[end_idx] != current_num:
            return end_idx - 1
    return len(boom_list) - 1

while True:
    did_explode = False
    
    for idx, value in enumerate(boom_list):
        if value == 0:
            continue
        end_idx = end_idx_return(idx, value)
        
        if end_idx - idx + 1 >= m:
            boom_list[idx:end_idx + 1] = [0] * (end_idx - idx + 1)
            did_explode = True
    boom_list = list(filter(lambda x: x > 0, boom_list))
    
    if not did_explode:
        break
print(len(boom_list))
for num in boom_list:
    print(num)
