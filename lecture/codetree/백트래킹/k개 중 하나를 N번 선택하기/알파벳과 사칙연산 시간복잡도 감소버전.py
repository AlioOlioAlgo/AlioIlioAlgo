"""
 *packageName    :
 * fileName       : 알파벳과 사칙연산
 * author         : ipeac
 * date           : 2023-01-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-29        ipeac       최초 생성
 """

max_value = 0
alpha_order = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5
}
input_value = list(input())

alpha = []
op = []
op_cnt = 0
for value in input_value:
    if value.isalpha():
        alpha.append(value)
    else:
        op_cnt += 1
        op.append(value)

ans = -1e9

def calc(combi):
    value = combi[alpha_order[alpha[0]]]
    for op_idx in range(op_cnt):
        if op[op_idx] == "+":
            value += combi[alpha_order[alpha[op_idx + 1]]]
        elif op[op_idx] == "-":
            value -= combi[alpha_order[alpha[op_idx + 1]]]
        else:
            value *= combi[alpha_order[alpha[op_idx + 1]]]
    
    return value

combi = []

def make_permutations(cnt):
    global max_value
    if cnt == 6:
        max_value = max(max_value, calc(combi))
        return
    for i in range(1, 5):
        combi.append(i)
        make_permutations(cnt + 1)
        combi.pop()

make_permutations(0)
print(max_value)
