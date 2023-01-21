"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-12-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-12-24        ipeac       최초 생성
 """
a_count, b_count = map(int, input().split())  # a,b 의 원소의 개수 빈 칸을 두고 주어진다.
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))

a_b_count = len(a.difference(b))
b_a_count = len(b - a)

print(a_b_count + b_a_count)
