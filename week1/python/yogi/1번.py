"""
 *packageName    : 
 * fileName       : 1번
 * author         : ipeac
 * date           : 2022-10-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-21        ipeac       최초 생성
 """
import heapq

def solution(stack1, stack2, stack3):
    answer = []
    
    new_stack = []
    new_stack.extend(stack1)
    new_stack.extend(stack2)
    new_stack.extend(stack3)
    max_heap = []
    for i in new_stack:
        heapq.heappush(max_heap, -i)
    while len(stack1) >= 1 or len(stack2) >= 1 or len(stack3) >= 1:
        print(f"max_heap = {max_heap}")
        poped_value = heapq.heappop(max_heap)
        poped_value = -poped_value
        if stack1 and poped_value == stack1[-1]:
            answer.append(1)
            stack1.pop()
        if stack2 and poped_value == stack2[-1]:
            answer.append(2)
            stack2.pop()
        if stack3 and poped_value == stack3[-1]:
            answer.append(3)
            stack3.pop()
    str_answer = ''
    for i in answer:
        str_answer += str(i)
    
    return str_answer

print(solution([2, 7], [4, 5], [1]))  # 12213
print(solution([10, 20, 30], [8], [1]))  # 11123
print(solution([7], [], [9]))  # 31
