"""
 *packageName    :
 * fileName       : [PCCP 모의고사 #1]유전 법칙
 * author         : ipeac
 * date           : 2022-12-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-25        ipeac       최초 생성
 """
import math
import sys

sys.setrecursionlimit(10 ** 6)

def solution(queries):
    print("==========================================")
    answer = []
    
    def dfs(index_p):
        if index_p == 0:
            return
        stack.append(index_p)
        dfs((index_p - 1) // 4)
    
    def find_child(stack):  # [9  , 2]
        pop_value = stack.pop()  # 2 -> 9
        index_value = pop_value % 4
        print(f"index_value = {index_value}")
        
        if index_value == 1:
            answer.append("RR")
            return
        elif 2 <= index_value <= 3:  # 2 ->
            if not stack:
                answer.append("Rr")
                print(f"answer = {answer}")
                return
            else:
                find_child(stack)
        
        else:
            answer.append("rr")
    
    for query in queries:
        # 인덱스는 1부터 시작합니다,.
        generation, index = map(int, query)
        if generation == 1:
            answer.append("Rr")
            continue
        
        prod = ((math.pow(4, generation - 1) - 1) // (4 - 1))
        print(f"prod = {prod}")
        index += int(prod - 1)
        print(f"index = {index}")
        # 인덱스  10
        #  9로 치환
        stack = []
        dfs(index)
        print(f"stack = {stack}")
        find_child(stack)
    return answer

print(solution([[3, 5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))
print(solution([[1, 1]]))
print(solution([[2, 1], [2, 2], [2, 3], [2, 4]]))
print(solution([[3, 4], [3, 6], [3, 7], [3, 8], [3, 9]]))
print(solution([[4, 20]]))
solution([[3, 8], [2, 2]])
solution([[3, 1], [2, 3], [3, 9]])
solution([[4, 26]])
