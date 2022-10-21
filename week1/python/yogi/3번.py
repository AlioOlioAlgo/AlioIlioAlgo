"""
 *packageName    : 
 * fileName       : 3번
 * author         : ipeac
 * date           : 2022-10-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-21        ipeac       최초 생성
 """

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter

def solution(S, C):
    for i in range(len(C)):
        flag = True
        list_s = list(S)
        
        enu = S.split("$")
        for value in enu:
            # 검증
            word = Counter(value).most_common()
            if word[0][1] >= 2:
                list_s.insert(C[i], '$')
                S = ''.join(list_s)
                flag = False
        if flag:
            return i - 1
        
        pass

print(solution("aabcba", [1, 3, 2]))  # 2
# print("aaa", [1, 2]) # 2
# print("wkwk", [1])  # -1
# print("abcd", [1, 2])  # 0
