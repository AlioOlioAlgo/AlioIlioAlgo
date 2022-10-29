"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-29        ipeac       최초 생성
 """
# n = int(input())
# scv = list(map(int, input().split()))
# dp = [i for i in range(n)]
# print(f"n = {n}")
# print(f"scv = {scv}")
# print(f"dp = {dp}")

n = 3
scv = [12, 10, 4]

while len(scv) < 3:
    scv += [0]
ans = 100
dp = [[[100] * (max(scv) + 1)]]

def answer(x, y, z, cnt):
    global ans
