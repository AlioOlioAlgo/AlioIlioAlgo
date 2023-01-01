"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-12        ipeac       최초 생성
 """
n = int(input())

numlist = sorted((list(map(int, input().split())) for _ in range(n)))
length = numlist[0][1] - numlist[0][0]
target = numlist[0][1]

for idx in range(1, len(numlist)):
    if numlist[idx][1] <= target:
        continue
    
    elif numlist[idx][0] < target < numlist[idx][1]:
        length += numlist[idx][1] - target  # 2
        target = numlist[idx][1]
    
    elif target <= numlist[idx][0]:
        length += numlist[idx][1] - numlist[idx][0]
        target = numlist[idx][1]
print(length)
