"""
 *packageName    :
 * fileName       : 금 채굴하기
 * author         : ipeac
 * date           : 2022-12-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-29        ipeac       최초 생성
 """
n, m = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
k = 2 * (n - 1)  # k 만큼의 마름모의 크기를 최대로 가집니다.

# 1번 인덱스부터 돌기 시작합니다.
def get_num_of_gold(row, col, k):
    sum = 0
    for i in range(n):
        for j in range(n):
            if abs(row - i) + abs(col - j) <= k:
                sum += graph[i][j]
    return sum

max_value = 0
for row in range(n):
    for col in range(n):
        for k in range(2 * (n - 1) + 1):
            num_of_gold = get_num_of_gold(row, col, k)
            
            if num_of_gold * m >= k * k + (k + 1) * (k + 1):
                max_value = max(max_value, num_of_gold)
print(max_value)
