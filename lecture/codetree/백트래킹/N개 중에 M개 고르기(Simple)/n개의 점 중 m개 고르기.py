"""
 *packageName    : 
 * fileName       : n개의 점 중 m개 고르기
 * author         : ipeac
 * date           : 2023-02-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-07        ipeac       최초 생성
"""
n, m = map(int, input().split())

min_value = 1e9

input_arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr = []

def iterable_function():
    max_value = -1e9
    # 선택한 점들 중 거리가 가장 먼 두 점을 구해야합니다.
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            max_value = max(max_value, distance_calc(arr[i][0], arr[j][0], arr[i][1], arr[j][1]))
    
    return max_value

def distance_calc(x1, x2, y1, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1 / 2)

def make_point(idx, cnt):
    global min_value
    if cnt == m:
        min_value = min(min_value, iterable_function())
        return
    if idx == n:
        return
    arr.append(input_arr[idx])
    make_point(idx + 1, cnt + 1)
    arr.pop()
    make_point(idx + 1, cnt)

make_point(0, 0)
print(int(min_value ** 2))
