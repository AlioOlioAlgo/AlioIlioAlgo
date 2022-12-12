"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-11        ipeac       최초 생성
 """
n = int(input())
string = list(map(str, input()))
stack = []
check = [0] * n

for idx, value in enumerate(string):
    if value == '(':
        stack.append(idx)
    else:
        if stack:
            check[idx], check[stack[-1]] = 1, 1
            stack.pop()
            print(f"check = {check}")
print(f"check = {check}")

max_length = 0
tmp = 0
for value in check:
    if value == 1:
        tmp += 1
    else:
        max_length = max(tmp, max_length)
        tmp = 0
print(max(max_length, tmp))
