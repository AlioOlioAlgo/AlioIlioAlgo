"""
 *packageName    : 
 * fileName       : 2번
 * author         : ipeac
 * date           : 2023-03-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-18        ipeac       최초 생성
"""

def solution(S):
    n = len(S)
    left = 0
    right = 0
    max_length = 0
    
    for i in range(n):
        if S[i] == '<' or S[i] == '?':
            left += 1
        elif S[i] == '>' or S[i] == '?':
            right += 1
        
        if left == right:
            max_length = max(max_length, 2 * right)
        
        if right > left:
            left = 0
            right = 0
    
    left = 0
    right = 0
    
    for i in range(n - 1, -1, -1):
        if S[i] == '>' or S[i] == '?':
            right += 1
        elif S[i] == '<' or S[i] == '?':
            left += 1
        
        if left == right:
            max_length = max(max_length, 2 * left)
        
        if left > right:
            left = 0
            right = 0
    
    return max_length

# 예제 사용:
# S1 = "<><??>>"
# print(solution(S1))  # 출력: 4

S2 = "??????"
print(solution(S2))  # 출력: 6

S3 = "<<?"
print(solution(S3))  # 출력: 2
