"""
 *packageName    : 
 * fileName       : 세 수의 합
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
dic = dict()

for value in arr:
    if value in dic:
        dic[value] += 1
    else:
        dic[value] = 1
ans = 0
for i in range(n):
    dic[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]
        if diff in dic:
            ans += dic[diff]
print(ans)
