"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-11-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-01        ipeac       최초 생성
 """
# https://www.acmicpc.net/problem/16637
import sys

input = sys.stdin.readline

result = int(-1e9)

n = 9
expr = '3+8*7-9*2'
num, op = [], []

def calc(num, op):  # 남은 수식을 전부 계산하는 함수
    while op:
        oper = op.pop(0)
        n1, n2 = num.pop(0), num.pop(0)
        if oper == '+':
            num.insert(0, n1 + n2)
        elif oper == '-':
            num.insert(0, n1 - n2)
        elif oper == '*':
            num.insert(0, n1 * n2)
    return num[0]

def solve(cnt, num, op):
    global result
    if cnt == n // 2 or len(num) == 1:  # 수식의 끝까지 도달했거나, 남은 피연산자가 1개인 경우 종료한다.
        result = max(result, calc(num, op))
        return
    solve(cnt + 1, num[:], op[:])  # 이번 연산자를 계산전에 미리 하나 뒤로 보내줌 (모든 경우의수 대비)
    
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

for i in range(n):  # 연산자와 피 연산자를 나누어 저장
    if i % 2 == 0:
        num.append(int(expr[i]))
    else:
        op.append(expr[i])

solve(0, num, op)
print(result)
