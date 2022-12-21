"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-12-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-17        ipeac       최초 생성
 """
import math
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

colors = [
    int(input())
    for _ in range(m)
]

print(f"colors = {colors}")

def binary_search(low, high):
    answer = int(1e9)
    while low <= high:
        tmp = 0
        mid = (low + high) // 2
        for count in colors:
            tmp += math.ceil(count / mid)
        if tmp > n:
            low = mid + 1
        else:
            high = mid - 1
            answer = min(answer, mid)  # mid 나눌수 있는 값 => 질투값
    return answer

print(binary_search(1, max(colors)))
