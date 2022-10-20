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
# list index로 탐색했을때 시간초과가 나왔다.
# 리스트 순회 탐색의 경우 O(n)
# 맵의 경우
# O(1) 로서
#
# 포켓몬 배열이 길면길수록 시간이 오래걸림.
#
# 연산	시간 복잡도	설명
# len(a)	O(1)	요소의 개수를 리턴한다.
# a[key]	O(1)	키를 조회하여 값을 리턴한다.
# a[key] = value	O(1)	키/값을 삽입한다.
# key in a	O(1)	딕셔너리에 키가 존재하는지 확인한다
