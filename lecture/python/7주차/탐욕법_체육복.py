"""
 *packageName    :
 * fileName       : 탐욕법_체육복
 * author         : ipeac
 * date           : 2023-01-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-08        ipeac       최초 생성
 """

"""
n : 전체 학생의 수
lost : 체육복 도난당한 학생
reserve : 체육복 여벌있는 학생
"""

def solution(n, lost, reserve):
    # 교집합 삭제 - 여벌 가진 학생이 잃어버릴수도있다.
    lost = set(lost)
    reserve = set(reserve)
    same = reserve.intersection(lost)
    lost -= same
    reserve -= same
    lost = list(lost)
    reserve = list(reserve)
    
    # 정렬오 오름차순 비교가능하도록
    lost.sort()
    reserve.sort()
    
    losted = len(lost)
    reserved = len(reserve)
    
    print(f"lost = {lost}")
    print(f"reserve = {reserve}")
    
    for lost_person in lost:
        for reseve_person in reserve:
            if lost_person - 1 == reseve_person:
                reserve.remove(reseve_person)
                break
            elif lost_person + 1 == reseve_person:
                reserve.remove(reseve_person)
                break
    print(f"lost = {lost}")
    print(f"reserve = {reserve}")
    now_then = n - losted
    now_then += reserved - len(reserve)
    print(f"now_then = {now_then}")
    return now_then

print("==========================================")
solution(5, [2, 4], [1, 3, 5])
print("==========================================")
solution(5, [2, 4], [3])
print("==========================================")
solution(3, [3], [1])
