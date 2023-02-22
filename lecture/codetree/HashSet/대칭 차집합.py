"""
 *packageName    : 
 * fileName       : 대칭 차집합
 * author         : ipeac
 * date           : 2023-02-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-02-20        ipeac       최초 생성
"""
a_cnt, b_cnt = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
aa = a - b
bb = b - a
print(len(aa | bb))
