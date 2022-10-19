"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-19        ipeac       최초 생성
 """
a, b, c = map(int, input().split())
time = []

# 최대 배열을 선언하기 위한 max_time
max_time = -1e9

for i in range(3):
    l = list(map(int, input().split()))
    # 배열선을 위해 최대값을 찾아야 하기에 입력받은 한 줄에서 max 값을 구하고
    # 해당 값이 max_time 보다 크다면  max_time에 대입합니다.
    if max_time < max(l):
        max_time = max(l)
    time.append(l)

# 한대 요금 2대 요금 3개 요금
# a, b, c = (5, 3, 1)
# 차가 들어간 시간 나온시간 리스트
# time = [[1, 6], [3, 5], [2, 8]]


arr = [0 for _ in range(max_time + 1)] #맥스 타임만큼의 배열 선언
answer = 0

for start, end in time:
    for i in range(start, end): # 입력받은 start ,end -1 타임까지 시간 배열에 count합니다.
        arr[i] += 1
for value in arr:
    # 시간배열에 1 이라면 1대의 차
    # 2 라면 2대의차
    # 3 이라면 3대의 차가 존재합니다. 이후 대수에 맞춰서 연산합니다.
    if value == 1:
        answer += value * a
    elif value == 2:
        answer += value * b
    else:
        answer += value * c
print(answer)

# 시간복잡도 O(n^2)
