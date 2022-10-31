"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-31        ipeac       최초 생성
 """
k = int(input())
build = list(map(int, input().split()))
# print(f"k = {k}")
# print(f"build = {build}")
# k = 3
# build = [1, 6, 4, 3, 5, 2, 7]
ans = [[] for _ in range(k)]

def dp(list_of, cnt):
    if len(list_of) < 3:
        ans[cnt].append(list_of[0])
        return
    else:
        ans[cnt].append(list_of[len(list_of) // 2])
        
        dp(list_of[:len(list_of) // 2], cnt + 1)
        dp(list_of[len(list_of) // 2 + 1:], cnt + 1)

dp(build, 0)

for value in ans:
    print(*value)
