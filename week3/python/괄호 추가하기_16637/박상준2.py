"""
 *packageName    :
 * fileName       : 박상준2
 * author         : ipeac
 * date           : 2022-11-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-11        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline

result = -2 ** 31 - 1

def calc(num, op):
    while op:
        oper = op.pop(0)
        n1, n2 = num.pop(0), num.pop(0),
        if oper == '+':
            num.insert(0, n1 + n2)
        elif oper == '-':
            num.insert(0, n1 - n2)
        elif oper == '*':
            num.insert(0, n1 * n2)
    return num[0]

def solve(cnt, num, op):
    global result
    if cnt == n // 2 or len(num) == 1:  # 수식의 끝에 도달했거나, 남은 피연산자가 1개인 경우 종료
        result = max(result, calc(num, op))
        return
    
    solve(cnt + 1, num[:], op[:])  # 이번 연산자를 계산전에 미리 하나 뒤로 보내줌(모든 경우의 수 대비)
    
    try:
        n1, n2 = num.pop(cnt), num.pop(cnt)
        oper = op.pop(cnt)
        if oper == '+':
            num.insert(cnt, n1 + n2)
        elif oper == '-':
            num.insert(cnt, n1 - n2)
        elif oper == '*':
            num.insert(cnt, n1 * n2)
        
        solve(cnt + 1, num[:], op[:])
    except:
        pass

n = int(input())
# n = 1
expr = input()
# expr = '1'
num, op = [], []

for i in range(n):
    if i % 2 == 0:
        num.append(int(expr[i]))
    else:
        op.append(expr[i])

solve(0, num, op)
print(result)
