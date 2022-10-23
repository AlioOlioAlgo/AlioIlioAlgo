"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-23        ipeac       최초 생성
 """
n, m = map(int, input().split())
apples = []
for _ in range(j := int(input())):
    apples.append(int(input()))
# print(f"n,m = {n, m}")
# print(f"apples = {apples}")
# n, m = (5, 2)
# j = 3
# apples = [1, 5, 3]

start = 1
end = m
cnt = 0
for word in apples:
    while True:
        if start <= word <= end:
            break
        elif word < start:
            start -= 1
            end -= 1
        elif end < word:
            start += 1
            end += 1
        cnt += 1

print(cnt)
