"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-24        ipeac       최초 생성
 """
t = 3
nums = [3, 60, 100]
# for _ in range(t):
for num in nums:
    cnt = 0
    
    i = 5
    while i <= num:
        cnt += num // i
        i *= 5
    print(cnt)
