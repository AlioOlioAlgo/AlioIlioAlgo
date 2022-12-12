"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-12        ipeac       최초 생성
 """
from collections import defaultdict

def get_pizza_sum(size, pizza, pizza_dict):
    print("====================get_pizza_sum======================")
    for i in range(size):
        print("=====================i====================")
        pizza_sum = pizza[i]
        pizza_dict[pizza_sum] += 1
        print(f"pizza_sum = {pizza_sum}")
        print(f"pizza_dict = {pizza_dict}")
        
        for j in range(1, size - 1):  # 시작 피자 조각에서 j 개의 피자 조각을 더 사용하는 경우
            pizza_sum += pizza[i + j]
            pizza_dict[pizza_sum] += 1
            print(f"pizza_sum = {pizza_sum}")
            print(f"pizza_dict = {pizza_dict}")
    pizza_dict[0] += 1  # 하나의 피자 조각도 사용하지 않는 경우
    pizza_dict[sum(pizza)] += 1  # 모든 피자 조각을 사용한 경우

target = int(input())  # 고객이 원하는 피자의 크기
m, n = map(int, input().split())  # m A 피자의 조각수 ||  n  B 피자의 조각수
aPizzaDict, bPizzaDict = defaultdict(int), defaultdict(int)  # 각 피자의 경우의 수를 카운트

aPizza = [
    int(input())
    for _ in range(m)
]

bPizza = [
    int(input())
    for _ in range(n)
]

print(f"aPizza = {aPizza}")
print(f"bPizza = {bPizza}")

sum_a_pizza = aPizza + aPizza
sum_b_pizza = bPizza + bPizza

get_pizza_sum(m, sum_a_pizza, aPizzaDict)
get_pizza_sum(n, sum_b_pizza, bPizzaDict)

ans = 0
for i in range(target + 1):
    ans += aPizzaDict[i] * bPizzaDict[target - i]
print(ans)
