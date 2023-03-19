"""
 *packageName    :
 * fileName       : 최단 Run Length 인코딩
 * author         : ipeac
 * date           : 2022-12-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-31        ipeac       최초 생성
 """
import itertools
import sys
from collections import deque

string = deque(list(input()))
min_length = int(1e9)
if len(string) == 1:
    print(2)
    sys.exit(0)
for _ in range(len(string) - 1):
    string.rotate(1)
    tmp_string = []
    first = string[0]
    same_cnt = 1
    for index in range(1, len(string)):
        if string[index] == first:
            same_cnt += 1
        
        elif string[index] != first:
            tmp_string += list(str(same_cnt)) + list(itertools.islice(string, index - 1, index))
            same_cnt = 1
            first = string[index]
        if index == len(string) - 1:
            tmp_string += list(str(same_cnt)) + list(itertools.islice(string, index, index + 1))
    
    min_length = min(len(tmp_string), min_length)
print(min_length)
