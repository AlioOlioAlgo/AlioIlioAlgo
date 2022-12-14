"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-14        ipeac       최초 생성
 """
n = int(input())
numbers = list(map(int, input().split()))
end = 0
cnt = 0
visited = [0] * 100001

for st in range(n):  # 1 2 3 1 2
    # print("==========================================")
    # print(f"st = {st}")
    while end < n:  #
        if visited[numbers[end]]:
            break
        # print(f"numbers = {numbers[end]}")
        visited[numbers[end]] = 1
        end += 1
    cnt += end - st
    visited[numbers[st]] = 0
    # print(f"cnt = {cnt}")

print(cnt)
