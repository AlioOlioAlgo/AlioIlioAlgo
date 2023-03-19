"""
 *packageName    :
 * fileName       : 특정 조건에 맞게 k개 중에 1개를 n번 뽑기
 * author         : ipeac
 * date           : 2023-01-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-30        ipeac       최초 생성
 """
k, n = map(int, input().split())
lister = []

def print_it():
    for li in lister:
        print(li, end=" ")
    print()

def make_number(cnt):
    if cnt == n:
        print_it()
        return
    for i in range(1, k + 1):
        if len(lister) >= 2 and i == lister[-1] and lister[-1] == lister[-2]:
            continue
        lister.append(i)
        make_number(cnt + 1)
        lister.pop()

make_number(0)
