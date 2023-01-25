"""
 *packageName    :
 * fileName       : k개 중에 1개를 n번 뽑기
 * author         : ipeac
 * date           : 2023-01-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-01-25        ipeac       최초 생성
 """
k, n = map(int, input().split())
ans = []

def print_permutation():
    for num in ans:
        print(num, end=" ")
    print()

def find_permutation(cnt):
    if cnt == n:
        return print_permutation()
    
    for i in range(1, k + 1):
        ans.append(i)
        find_permutation(cnt + 1)
        ans.pop()

find_permutation(0)
