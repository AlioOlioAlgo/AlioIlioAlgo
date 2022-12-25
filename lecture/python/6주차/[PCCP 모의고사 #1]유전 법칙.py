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

def solution(queries):
    print("==========================================")
    answer = []
    
    for query in queries:
        # 인덱스는 1부터 시작합니다,.
        generation, index = map(int, query)
        if generation == 1:
            answer.append("Rr")
            continue
        
        bigger_group_end_index = math.pow(4, generation - 2)
        print(f"bigger_group_end_index = {bigger_group_end_index}")
        
        middle_group_end_index = 3 * (math.pow(4, generation - 2))
        print(f"middle_group_end_index = {middle_group_end_index}")
        
        smaller_group_end_index = 4 * (math.pow(4, generation - 2))
        print(f"smaller_group_end_index = {smaller_group_end_index}")
        
        if index <= bigger_group_end_index:
            answer.append("RR")
            pass
        elif index <= middle_group_end_index:
            index -= 1
            print(f"middle_group_end_index = {middle_group_end_index}")
            check = index % 4
            if not check:
                answer.append("RR")
            elif 1 <= check <= 2:
                answer.append("Rr")
            else:
                answer.append("rr")
        else:
            answer.append("rr")
            pass
    
    return answer

print(solution([[3, 5]]))
print(solution([[3, 8], [2, 2]]))
print(solution([[3, 1], [2, 3], [3, 9]]))
print(solution([[4, 26]]))
print(solution([[1, 1]]))
print(solution([[2, 1], [2, 2], [2, 3], [2, 4]]))
print(solution([[3, 4], [3, 6], [3, 7], [3, 8], [3, 9]]))
# solution([[3, 8], [2, 2]])
# solution([[3, 1], [2, 3], [3, 9]])
# solution([[4, 26]])
