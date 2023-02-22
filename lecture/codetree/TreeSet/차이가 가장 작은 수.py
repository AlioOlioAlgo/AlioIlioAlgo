"""
 *packageName    : 
 * fileName       : 차이가 가장 작은 수
 * author         : ipeac
 * date           : 2023-02-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-23        ipeac       최초 생성
"""
n, m = map(int, input().split())
arr = [
    int(input())
    for _ in range(n)
]
arr.sort()
ans = 1e9

# 각 인덱스를 기준으로,  m이상의 차이를 갖는 수 중에서 가장 작은 값을 탐색합니다.
for i in range(n):
    left, right = i + 1, n - 1
    while left <= right:
        mid = (left + right) // 2
        diff = arr[mid] - arr[i]
        if diff >= m:
            # 차이가  m 이상인 경우, 현재까지의 최솟값과 비교하여 갱신합니다
            ans = min(ans, diff)
            right = mid - 1
        else:
            left = mid + 1

print(ans)
