"""
 *packageName    : 
 * fileName       : 1번
 * author         : ipeac
 * date           : 2023-03-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-18        ipeac       최초 생성
"""
from collections import Counter

def solution(s):
    counts = Counter(s)
    print(f"counts  ==> {counts}")
    
    delect_cnt = 0
    
    for value in counts.values():
        if value % 2 == 1:
            delect_cnt += 1
    
    return delect_cnt

print(solution("acbcbba"))  # 1
print(solution("axxaxa"))  # 2
print(solution("aaaa"))  # 0
