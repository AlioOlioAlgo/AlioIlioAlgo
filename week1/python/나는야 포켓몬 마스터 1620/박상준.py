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
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 포켓몬 딕셔너리
pokemons = {}
for i in range(n):
    # 딕셔너리의 인덱스와 해당 밸류를 둘다 담아준다.
    value = input().rstrip()
    pokemons[i] = value
    pokemons[value] = i

for i in range(m):
    test = input().rstrip()
    # 테스트값이 숫자라면 해당 숫자에 해당하는 포켓몬 ㄱㄱ
    if test.isnumeric():
        print(pokemons[int(test) - 1])
    # 반대
    else:
        print(pokemons[test] + 1)
