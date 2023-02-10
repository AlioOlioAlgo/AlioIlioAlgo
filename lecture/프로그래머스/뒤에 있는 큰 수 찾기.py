"""
 *packageName    : 
 * fileName       : 뒤에 있는 큰 수 찾기
 * author         : ipeac
 * date           : 2023-02-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-10        ipeac       최초 생성
 """

def solution(numbers):
    answer = []
    # 큐 + 스택
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        print(f"i  ==> {i}")
        print(f"stack  ==> {stack}")
        while len(stack) != 0:
            if stack[-1] > numbers[i]:
                answer.append(stack[-1])
                break
            else:
                stack.pop()
        if len(stack) == 0:
            answer.append(-1)
        stack.append(numbers[i])
    answer.reverse()
    return answer

print(solution([2, 3, 3, 5]))
# solution([9, 1, 5, 3, 6, 2])
