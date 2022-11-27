"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-23        ipeac       최초 생성
 """
n = int(input())  # 목표 값
a = [False, False] + [True] * (n - 1)
# print(f"a = {a}")
max_cnt = 0
prime = []
# 에라스 체
for i in range(2, n + 1):
    if a[i]:
        prime.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

# print(f"a = {a}")
# print(f"prime = {prime}")
start = 0
end = 0
while end <= len(prime):
    # print("==========================================")
    # print(f"start = {start}")
    # print(f"end = {end}")
    sum_sub = sum(prime[start:end])
    # print(f"sum_sub = {sum_sub}")
    if sum_sub > n:
        start += 1
    elif sum_sub < n:
        end += 1
    else:
        start += 1
        max_cnt += 1
print(max_cnt)
