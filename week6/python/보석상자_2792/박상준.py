"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-14        ipeac       최초 생성
 """
# import math, sys
#
# input = sys.stdin.readline
# N, M = map(int, input().split())
# jew = []
# for _ in range(M):
#     jew.append(int(input()))
#
# def binary_search(low, high):
#     dab = 999999999
#     while low <= high:
#         tmp = 0
#         mid = (low + high) // 2
#         for i in jew:
#             tmp += math.ceil(i / mid)
#
#         if tmp > N:
#             low = mid + 1
#         else:
#             high = mid - 1
#             dab = min(dab, mid)
#     return dab
#
# print(binary_search(1, max(jew)))
