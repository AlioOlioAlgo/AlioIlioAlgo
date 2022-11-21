"""
 *packageName    :
 * fileName       : 기초3-1
 * author         : ipeac
 * date           : 2022-11-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-11-20        ipeac       최초 생성
 """
# num = list(map(int, input().split()))
# button = int(input())
#
# if button == 1 or button == 2:
#     print(num[button - 1])

# score = list(map(int, input().split()))
# # 최대 힙  n log n >>  n >> log n >> 1
# print(max(score))
# print(sum(score) // len(score))
# print(score[0])

"""
2 7 11 15
9
output : [0,1]
--
3 2 4
6
[1,2]
--
3 3
6
[0,1]
"""
nums = list(map(int, input().split()))
target = int(input())
