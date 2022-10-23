"""
 *packageName    :
 * fileName       : 박상준
 * author         : ipeac
 * date           : 2022-10-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-19        ipeac       최초 생성
 """
from collections import defaultdict

n = int(input())
words = [
    input()
    for _ in range(n)
]

# n = 18
# words = ['babic', 'keksic', 'boric', 'bukic', 'sarmic', 'balic', 'kruzic', 'hrenovkic', 'beslic', 'boksic', 'krafnic', 'pecivic', 'klavirkovic', 'kukumaric', 'sunkic', 'kolacic', 'kovacic', 'prijestolonasljednikovi']
# 딕셔너리 생성
dic = defaultdict(int)

# 5 이상 반복되는 성을 담을 배열
answer = []

# 단어를 반복
for word in words:
    # default_dict의 경우 키값을 미리 정의해주지 않더라고 대입시점에 int = 0으로 초기화시켜줌
    # 해당 성의 키값+1
    dic[word[:1]] += 1
    
# 아이템 중에 value 가 5이상인 값을 answer에 담고
for key, value, in dic.items():
    if value >= 5:
        answer.append(key)
        
# 길이가 0이라면
if len(answer) == 0:
    print("PREDAJA")
else:
    # 사전순으로 정렬해야함
    answer.sort()
    
    for value in answer:
        print(value, end="")
