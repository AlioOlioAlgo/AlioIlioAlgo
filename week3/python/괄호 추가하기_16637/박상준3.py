"""
 *packageName    :
 * fileName       : 박상준3
 * author         : ipeac
 * date           : 2022-11-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-19        ipeac       최초 생성
 """
from math import inf
from sys import stdin

def dfs(idx, sub_total):
    print("==========================================")
    print(f"idx = {idx}")
    print(f"sub_total = {sub_total}")
    print(f"nums = {nums}")
    print(f"op = {op}")
    
    global answer
    
    if idx == len(op):
        answer = max(answer, int(sub_total))
        print(f"answer = {answer}")
        return
    
    # (3 + 8) * 7 - 9 * 2 부터 시작.
    first = str(eval(sub_total + op[idx] + nums[idx + 1]))
    print(f"first = {first}")
    dfs(idx + 1, first)
    
    if idx + 1 < len(op):
        # 3 + (8 * 7) - 9 * 2 부터 시작
        second = str(eval(nums[idx + 1] + op[idx + 1] + nums[idx + 2]))
        print(f"second = {second}")
        second = str(eval(sub_total + op[idx] + second))
        print(f"second = {second}")
        # op를 2개 소모했으므로 idx + 2
        dfs(idx + 2, second)

if __name__ == '__main__':
    n = int(stdin.readline())
    expression = stdin.readline().rstrip()
    nums, op = [], []
    answer = -inf
    
    for e in expression:
        nums.append(e) if e.isdigit() else op.append(e)
    
    print(f"nums = {nums}")
    print(f"op = {op}")
    dfs(0, nums[0])
    print(answer)
