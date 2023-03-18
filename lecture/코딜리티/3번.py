"""
 *packageName    : 
 * fileName       : 3번
 * author         : ipeac
 * date           : 2023-03-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-18        ipeac       최초 생성
"""

def solution(s):
    left, right, cnt = 0, 0, 0
    max_len = 0
    for value in s:
        if value == '<':
            left += 1
        elif value == '>':
            right += 1
        elif value == '?':
            cnt += 1
        if right > left + cnt:
            left, right, cnt = 0, 0, 0
        max_len = max(max_len, left + right)
    print(f"max_len  ==> {max_len}")
    left, right, cnt = 0, 0, 0
    
    for value in reversed(s):
        if value == '<':
            left += 1
        elif value == '>':
            right += 1
        elif value == '?':
            cnt += 1
        if left > right + cnt:
            left, right, cnt = 0, 0, 0
        max_len = max(max_len, left + right)
    print(f"max_len  ==> {max_len}")
    return max_len

print(solution("<><??>>"))
print(solution("??????"))
print(solution("<<?"))
