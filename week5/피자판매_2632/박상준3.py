"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2023-01-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-08        ipeac       최초 생성
 """
from collections import defaultdict

pizza_size = int(input())
m, n = map(int, input().split())
pizza_a = [
    int(input())
    for _ in range(m)
]
pizza_b = [
    int(input())
    for _ in range(n)
]
pizza_a_dict = defaultdict(int)
pizza_b_dict = defaultdict(int)

def get_pizza_sum(size, pizza, pizza_dict):
    for i in range(size):  # 시작 피자 조각
        pizza_sum = pizza[i]
        pizza_dict[pizza_sum] += 1
        
        for j in range(1, size - 1):  # 시작 피자 조각 +피자 조각 더 사용하는 경우
            pizza_sum += pizza[(i + j) % size]
            pizza_dict[pizza_sum] += 1
    pizza_dict[0] += 1  # 피자 조각 사용 X 경우
    pizza_dict[sum(pizza)] += 1

get_pizza_sum(m, pizza_a, pizza_a_dict)
get_pizza_sum(n, pizza_b, pizza_b_dict)
print(f"pizza_a_dict = {pizza_a_dict}")
print(f"pizza_b_dict = {pizza_b_dict}")
ans = 0
for i in range(pizza_size + 1):
    ans += pizza_a_dict[i] * pizza_b_dict[pizza_size - i]
print(ans)
