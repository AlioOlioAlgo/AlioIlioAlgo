"""
 *packageName    : 
 * fileName       : 자리 바꾸기2
 * author         : ipeac
 * date           : 2023-02-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-19        ipeac       최초 생성
"""
n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]

can_sit = [{i} for i in range(1, n + 1)]
switch_seat = [
    list(map(int, input().split()))
    for _ in range(k)
]
for i in range(3 * k):
    index = i % k
    can_sit[arr[switch_seat[index][0] - 1] - 1].add(switch_seat[index][1])
    can_sit[arr[switch_seat[index][1] - 1] - 1].add(switch_seat[index][0])
    arr[switch_seat[index][0] - 1], arr[switch_seat[index][1] - 1] = arr[switch_seat[index][1] - 1], arr[switch_seat[index][0] - 1]
for i in range(len(can_sit)):
    print(len(can_sit[i]))
