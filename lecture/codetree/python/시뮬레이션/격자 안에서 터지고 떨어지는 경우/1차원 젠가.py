"""
 *packageName    :
 * fileName       : 1차원 젠가
 * author         : ipeac
 * date           : 2023-01-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-01        ipeac       최초 생성
 """
n = int(input())
block = [
    int(input())
    for _ in range(n)
]

def cut_array(start, end):
    tmp_arr = []
    
    for i in range(len(block)):
        if i < start or i > end:
            tmp_arr.append(block[i])
    
    return tmp_arr

# 두번의 제거 과정을 걸칩니다.
for _ in range(2):
    s, e = map(int, input().split())
    block = cut_array(s - 1, e - 1)[:]
    # print(f"block = {block}")
print(len(block))
if len(block):
    for i in block:
        print(i)
