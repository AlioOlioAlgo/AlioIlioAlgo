"""
 *packageName    : 
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-21        ipeac       최초 생성
#  """
n = int(input())
m = int(input())
gapzu = list(map(int, input().split()))
#
# print(f"n = {n}")
# print(f"m = {m}")

# n = 6
# m = 9
# gapzu = [2, 7, 4, 1, 5, 3]
# n = 1
# m = 1
#
# gapzu = [1]
ans = 0
# 투포인터
# 가변적인 start end 가변적 공간
# 기준 배열이 sort 되어있어야 start end 로 정확한 값을 탐색가능
gapzu.sort()
start = 0
end = len(gapzu) - 1

# 갑주의 길이가 1 인경우
if len(gapzu) == 1:
    if gapzu[0] != m:
        print(0)
        exit()
    else:
        print(1)
        exit()
# 투포인터 start <= end 로 설정해서 start 와 end 가 겹치는 문제가 있었음
# 이후 수정
while start < end:
    sum_it = gapzu[start] + gapzu[end]
    # start end 인덱스의 값이  m이하면 start 값을 증가시켜야 해당 값을 맞출수있다,.
    if sum_it < m:
        start += 1
        # 위와 반대
    elif sum_it > m:
        end -= 1
    # 같다면 ans+=1 처리 및  start +1혹은 end -1 처리하면된다.
    else:
        ans += 1
        start += 1

print(ans)
