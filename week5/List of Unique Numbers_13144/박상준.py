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

"""
5
1 2 3 1 2

12
"""

n = int(input())
# n = 100000
arr = list(map(int, input().split()))
# arr = [i for i in range(1, 100001)]
cnt, end = 0, 0
check = [0] * 100001

for start in range(len(arr)):
    while end < n:
        if check[arr[end]] == 1:
            # 이미 방문한 경우는 안됨
            break
        check[arr[end]] = 1
        end += 1
    cnt += end - start
    check[arr[start]] = 0
print(cnt)
