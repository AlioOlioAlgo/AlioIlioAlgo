"""
 *packageName    : 
 * fileName       : 두 수의 합
 * author         : ipeac
 * date           : 2023-02-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-17        ipeac       최초 생성
 """
n, k = map(int, input().split())
arr = list(map(int, input().split()))
count = dict()

ans = 0

for value in arr:
    print("======================================================")
    print(f"value  ==> {value}")
    diff = k - value
    print(f"diff  ==> {diff}")
    print(f"count  ==> {count}")
    if diff in count:
        ans += count[diff]
    if value in count:
        count[value] += 1
    else:
        count[value] = 1

print(ans)
