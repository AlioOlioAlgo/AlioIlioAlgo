"""
 *packageName    :
 * fileName       : 겹치지 않게 선분 고르기
 * author         : ipeac
 * date           : 2023-01-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-28        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline
n = int(input())
input_data = [
    list(map(int, input().split()))
    for _ in range(n)
]
line = []

def dup_it(x, y, x1, y1):
    if x1 <= x <= y1 or x1 <= y <= y1 or x <= x1 <= y or x <= y1 <= y:
        return True  # 겹치는 친구가 존재합니다.
    return False

def check_dup():
    global line
    print(f"line = {line}")
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if dup_it(line[i][0], line[i][1], line[j][0], line[j][1]):
                return True
    return False  # 중복 없음

ans = 0

def process(idx):
    global ans
    if idx == n:
        if not check_dup():
            ans = max(ans, len(line))
            return ans
    
    for idx2 in range(idx, n):
        line.append(input_data[idx2])
        process(idx2 + 1)
        line.pop()
        process(idx2 + 1)

for i in range(n):
    line.append(input_data[i])
    process(i + 1)
    line.pop()

print(ans)
