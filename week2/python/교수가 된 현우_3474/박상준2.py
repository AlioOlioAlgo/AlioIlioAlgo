"""
 *packageName    : 
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-10-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-28        ipeac       최초 생성
 """
n = int(input())
count = 0
i = 5
while i <= n:
    count += n // i  # 60 /5 12 60 /25 2
    i *= 5
    print(f"i = {i}")
print(f"count = {count}")
