"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-30        ipeac       최초 생성
 """
from itertools import permutations

k = int(input())
inequality_sign = list(map(str, input().split()))
# print(f"k = {k}")
# print(f"inequality_sign = {inequality_sign}")

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 2
# inequality_sign = ['<', '>']
ans = []

for combi in permutations(num, len(inequality_sign) + 1):
    flag = True
    for idx in range(len(inequality_sign)):
        if inequality_sign[idx] == '<':
            if combi[idx] >= combi[idx + 1]:
                flag = False
                break
        elif inequality_sign[idx] == '>':
            if combi[idx] <= combi[idx + 1]:
                flag = False
                break
    if flag:
        ans.append(combi)
print(''.join(list(map(str, ans[-1]))))
print(''.join(list(map(str, ans[0]))))
