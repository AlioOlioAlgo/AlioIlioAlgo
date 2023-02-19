"""
 *packageName    : 
 * fileName       : C-TAG
 * author         : ipeac
 * date           : 2023-02-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-19        ipeac       최초 생성
"""
n, m = map(int, input().split())
a = [
    list(map(str, input()))
    for _ in range(n)
]
b = [
    list(map(str, input()))
    for _ in range(n)
]
ans = 0
a_set = set()

for i in range(m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            a_set.clear()
            for row in range(n):
                a_set.add(a[row][i] + a[row][j] + a[row][k])
            sw = False
            for row in range(n):
                string = b[row][i] + b[row][j] + b[row][k]
                if string in a_set:
                    sw = True
                    break
            if not sw:
                ans += 1
print(ans)
