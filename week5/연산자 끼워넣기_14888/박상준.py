"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-06        ipeac       최초 생성
 """
n = int(input())
numbers = list(map(int, input().split()))
operation = list(map(int, input().split()))
max_value = int(-1e9)
min_value = int(1e9)

def dfs(depth, total, operation):
    global max_value
    global min_value
    
    if depth == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    if operation[0]:  # 덧셈 수행 # 고려사항 없음
        operation[0] -= 1
        dfs(depth + 1, total + numbers[depth], operation)
        operation[0] += 1
    if operation[1]:  # 뺄셈 수행
        operation[1] -= 1
        dfs(depth + 1, total - numbers[depth], operation)
        operation[1] += 1
    if operation[2]:  # 곱하기
        operation[2] -= 1
        dfs(depth + 1, total * numbers[depth], operation)
        operation[2] += 1
    if operation[3]:  # 나눗셈 > 나눠지는 값이 음수인 경우 고려해야한다.
        operation[3] -= 1
        sum_total = total // numbers[depth]
        if total < 0 and numbers[depth] >= 0:
            total = -total
            sum_total = total // numbers[depth]
            sum_total = -sum_total
        
        dfs(depth + 1, sum_total, operation)
        operation[3] += 1

dfs(1, numbers[0], operation)
print(max_value)
print(min_value)
