# 입력 받기
n, c = map(int, input().split())
m = int(input())
boxes = []
for i in range(m):
    a, b, w = map(int, input().split())
    boxes.append((a, b, w))

# 도착지가 같은 경우 출발지가 먼저 오도록 정렬
boxes.sort(key=lambda x: (x[1], x[0]))

# 각 마을에서 현재까지 실을 수 있는 최대 무게 계산
capacity = [c] * (n + 1)
result = 0
for box in boxes:
    start, end, weight = box
    # 출발지부터 해당 마을까지의 거리에 따라 현재까지 운반한 무게 갱신
    max_weight = min(capacity[start], weight)
    for i in range(start + 1, end):
        max_weight = min(max_weight, capacity[i])
    if max_weight > 0:
        # 해당 마을에서 보낼 수 있는 택배의 무게 더해주기
        result += max_weight
        for i in range(start, end):
            capacity[i] -= max_weight

print(result)
