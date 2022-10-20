"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-19        ipeac       최초 생성
 """
s = input()
alpha_list = [0 for _ in range(26)]
# 26개의 배열 완성
#
for value in s:
    # 최솟값 a 의 아스키 코드값이 97입니다
    # 97 -97 으로 인덱스 0 번이 a 1번~~~~~~~ z 26 까지 카운트를 늘려줍니다.
    alpha_list[ord(value) - 97] += 1
# 리스트 출력
print(*alpha_list)

# 시간 복잡도 -> O(n)
