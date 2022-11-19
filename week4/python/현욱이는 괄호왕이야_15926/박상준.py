"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-14        ipeac       최초 생성
 """
n = int(input())
string = list(map(str, input()))
stack = []
check = [0] * n
# print(f"check = {check}")
for idx, value in enumerate(string):
    # print("==========================================")
    # print(f"value = {value}")
    if value == '(':
        stack.append(idx)
    else:
        if stack:
            check[idx], check[stack[-1]] = 1, 1
            stack.pop()
# print(f"check = {check}")
max_length = 0
tmp = 0
for value in check:
    if value == 1:
        tmp += 1
    else:
        max_length = max(max_length, tmp)
        tmp = 0
print(tmp if max_length == 0 else max_length)
