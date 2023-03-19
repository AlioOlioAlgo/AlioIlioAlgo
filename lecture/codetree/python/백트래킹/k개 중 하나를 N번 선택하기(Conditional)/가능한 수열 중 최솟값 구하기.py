"""
 *packageName    :
 * fileName       : 가능한 수열 중 최솟값 구하기
 * author         : ipeac
 * date           : 2023-01-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-31        ipeac       최초 생성
 """
import sys

n = int(input())  # 길이
list_n = []

def check():
    now_length = len(list_n)
    for i in range(1, now_length // 2 + 1):
        if list_n[-i:] == list_n[-i * 2: -i]:
            return True  # 같음
    return False

def make_sequence(cnt):
    if cnt == n:
        for num in list_n:
            print(num, end="")
        
        sys.exit()
    for i in range(4, 7):
        list_n.append(i)
        if len(list_n) >= 2 and check():
            list_n.pop()
            continue
        make_sequence(cnt + 1)
        list_n.pop()

make_sequence(0)
