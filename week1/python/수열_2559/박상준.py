"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-20        ipeac       최초 생성
 """
# 슬라이딩 윈도우 - 노 정렬 , 포인터 고정

n, k = map(int, input().split())
tempatures = list(map(int, input().split()))
# print(f"n,k = {n, k}")
# print(f"tempatures = {tempatures}")

# n, k = (10, 2)
# tempatures = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
max_value = -1e9
start = 0
curr_value = 0

for end, val in enumerate(tempatures):
    # 일단 최댓값 기산을 위해 상관없이 다 더한다.
    curr_value += val
    # end 값과 start 값 사이의 개수가 얼마인지 체크하기 위하여 end-start+1
    # k 값과 동일하다면 => ex ) k==2 라면 새롭게 최댓값 체크를 위함
    if end - start + 1 == k:
        max_value = max(max_value, curr_value)
        # 인덱스 0 1 를 계산했다면 -> k==2 성립 -> start=0 값을 빼고
        curr_value -= tempatures[start]
        
        # start 를 +1로 새로 설정
        start += 1
print(max_value)
