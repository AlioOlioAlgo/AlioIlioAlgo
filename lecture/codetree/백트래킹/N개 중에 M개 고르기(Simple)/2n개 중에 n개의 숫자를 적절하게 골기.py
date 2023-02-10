"""
*packageName    : ${PACKAGE_NAME}
* fileName       : ${NAME}
* author         : ${USER}
* date           : ${DATE}
* description    :
* ===========================================================
* DATE              AUTHOR             NOTE
* -----------------------------------------------------------
* ${DATE}        ${USER}       최초 생성
"""
n = int(input())
print("======================================================")
print(f"n  ==> {n}")

n2_list = list(map(int, input().split()))
visited = [False for _ in range(2 * n)]
print(f"n2_list  ==> {n2_list}")

min_value = 1e9


def calc():
    diff = 0
    for i in range(2 * n):
        diff = (diff + n2_list[i]) if visited[i] else diff - n2_list[i]
    return abs(diff)


def make_arr(idx, cnt):
    global min_value
    if cnt == n:
        min_value = min(min_value, calc())
        return
    if idx == 2 * n:
        return

    visited[idx] = True
    make_arr(idx + 1, cnt + 1)
    visited[idx] = False

    make_arr(idx + 1, cnt)


make_arr(0, 0)
print(min_value)
