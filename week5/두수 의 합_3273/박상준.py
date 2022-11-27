"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-24        ipeac       최초 생성
 """
n = int(input())
arr = list(map(int, input().split()))
target = int(input())
arr.sort()

# print(f"arr = {arr}")
start = 0
end = n - 1
cnt = 0
while start < end:
    sum_of = arr[start] + arr[end]
    if sum_of == target:
        cnt += 1
    elif sum_of < target:
        start += 1
        continue
    end -= 1
print(cnt)
